"""organizations module"""
import json
from datetime import datetime
from typing import TypedDict, List, NotRequired, Literal, Any, Union

import boto3
from boto3 import Session
from mypy_boto3_organizations import ListChildrenPaginator, ListParentsPaginator


# Type Defs and Type Literals

PolicyTypeType = Literal[
    "AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "SERVICE_CONTROL_POLICY", "TAG_POLICY"
]

PolicyTypeStatusType = Literal["ENABLED", "PENDING_DISABLE", "PENDING_ENABLE"]

ChildTypeType = Literal[
    "ACCOUNT",
    "ORGANIZATIONAL_UNIT",
]

AccountStatusType = Literal[
    "ACTIVE",
    "PENDING_CLOSURE",
    "SUSPENDED",
]

AccountJoinedMethodType = Literal[
    "CREATED",
    "INVITED",
]

ParentTypeType = Literal[
    "ORGANIZATIONAL_UNIT",
    "ROOT",
]

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": dict[str, str],
        "RetryAttempts": int,
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AccountStatusType],  # (1)
        "JoinedMethod": NotRequired[AccountJoinedMethodType],  # (2)
        "JoinedTimestamp": NotRequired[datetime],
    },
)

DescribeAccountResponseTypeDef = TypedDict(
    "DescribeAccountResponseTypeDef",
    {
        "Account": AccountTypeDef,  # (1)
        "ResponseMetadata": ResponseMetadataTypeDef,  # (2)
    },
)

ChildTypeDef = TypedDict(
    "ChildTypeDef", {"Id": NotRequired[str], "Type": NotRequired[ChildTypeType]}
)

ListChildrenResponseTypeDef = TypedDict(
    "ListChildrenResponseTypeDef",
    {
        "Children": List[ChildTypeDef],  # (1)
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {"Type": NotRequired[PolicyTypeType], "Status": NotRequired[PolicyTypeStatusType]},
)

RootTypeDef = TypedDict(
    "RootTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "PolicyTypes": NotRequired[List[PolicyTypeSummaryTypeDef]],
    },
)

ListRootsResponseTypeDef = TypedDict(
    "ListRootsResponseTypeDef",
    {
        "Roots": List[RootTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef",
    {"Id": NotRequired[str], "Arn": NotRequired[str], "Name": NotRequired[str]},
)

DescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "DescribeOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": OrganizationalUnitTypeDef,  # (1)
        "ResponseMetadata": ResponseMetadataTypeDef,  # (2)
    },
)

OrganizationalUnitBreakdownTypeDef = TypedDict(
    "OrganizationalUnitBreakdownTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Accounts": List[AccountTypeDef],
        "Children": List[Any],
    },
)

RootOrganizationalUnitBreakdownTypeDef = TypedDict(
    "RootOrganizationalUnitBreakdownTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Children": List[OrganizationalUnitBreakdownTypeDef],
    },
)

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ParentTypeType],  # (1)
    },
)

ListParentsResponseTypeDef = TypedDict(
    "ListParentsResponseTypeDef",
    {
        "Parents": List[ParentTypeDef],  # (1)
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,  # (2)
    },
)

DetailedAccountType = TypedDict(
    "DetailedAccountType",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": str,
        "JoinedMethod": str,
        "JoinedTimestamp": str,
        "Parent": str,
        "Path": str,
    },
)

# Variables

root_ou_breakdown: RootOrganizationalUnitBreakdownTypeDef = {}
flattened_accounts: List[DetailedAccountType] = []


# Functions


def describe_ou(
    session: Session, ou_id: str
) -> Union[DescribeOrganizationalUnitResponseTypeDef, str]:
    """Retrieves information about an organizational unit (OU).

    Args:
        session (Session): _description_
        ou_id (str): _description_

    Returns:
        Union[DescribeOrganizationalUnitResponseTypeDef, str]: _description_
    """
    org_client = session.client(service_name="organizations")
    try:
        response: Union[
            DescribeOrganizationalUnitResponseTypeDef, str
        ] = org_client.describe_organizational_unit(OrganizationalUnitId=ou_id)
        return response
    except (
        org_client.exceptions.AccessDeniedException,
        org_client.exceptions.AWSOrganizationsNotInUseException,
        org_client.exceptions.InvalidInputException,
        org_client.exceptions.OrganizationalUnitNotFoundException,
        org_client.exceptions.ServiceException,
        org_client.exceptions.TooManyRequestsException,
    ) as e:
        return str(object=e)


def describe_account(
    session: Session, account_id: str
) -> DescribeAccountResponseTypeDef:
    """Retrieves Organizations-related information about the specified account.

    Args:
        session (Session): _description_
        account_id (str): _description_

    Returns:
        DescribeAccountResponseTypeDef: _description_
    """

    org_client = session.client(service_name="organizations")
    try:
        response: DescribeAccountResponseTypeDef = org_client.describe_account(
            AccountId=account_id
        )
        return response
    except (
        org_client.exceptions.AccessDeniedException,
        org_client.exceptions.AccountNotFoundException,
        org_client.exceptions.AWSOrganizationsNotInUseException,
        org_client.exceptions.InvalidInputException,
        org_client.exceptions.ServiceException,
        org_client.exceptions.TooManyRequestsException,
    ) as e:
        return str(object=e)


def list_roots(session: Session) -> Union[ListRootsResponseTypeDef, str]:
    """Lists the roots that are defined in the current organization.

    Args:
        session (Session): A session stores configuration state and allows you
        to create service clients and resources.

    Returns:
        list: List of the roots that are defined in the current organization. List of dictionaries
    """
    org_client = session.client(service_name="organizations")

    try:
        response: Union[ListRootsResponseTypeDef, str] = org_client.list_roots()
        return response

    except (
        org_client.exceptions.AccessDeniedException,
        org_client.exceptions.AWSOrganizationsNotInUseException,
        org_client.exceptions.InvalidInputException,
        org_client.exceptions.ServiceException,
        org_client.exceptions.TooManyRequestsException
    ) as e:
        return str(object=e)


def list_children(
    session: Session, parent_id: str, child_type: Literal[ChildTypeType]
) -> Union[ListRootsResponseTypeDef, str]:
    """Lists the children that are defined in the current organization.

    Args:
        session (Session): A session stores configuration state and allows you
        to create service clients and resources.
        parent_id (str): The unique identifier (ID) of the root.

    Returns:
        list: List of the children that are defined in the
        current organization. List of dictionaries
    """

    child_list: list[ListChildrenResponseTypeDef] = []

    org_client = session.client(service_name="organizations")
    try:
        paginator: Union[ListChildrenPaginator, str] = org_client.get_paginator(
            "list_children",
        )

        for page in paginator.paginate(ParentId=parent_id, ChildType=child_type):
            # append individual ListChildrenResponseTypeDef to child_list
            for child in page["Children"]:
                child_list.append(child)

        return child_list

    except (
        org_client.exceptions.AccessDeniedException,
        org_client.exceptions.AWSOrganizationsNotInUseException,
        org_client.exceptions.InvalidInputException,
        org_client.exceptions.OrganizationalUnitNotFoundException,
        org_client.exceptions.ServiceException,
        org_client.exceptions.TooManyRequestsException,
    ) as e:
        return str(object=e)


def list_parents(session: Session, child_id: str) -> ListParentsResponseTypeDef:
    """_summary_

    Args:
        session (Session): _description_
        child_id (str): _description_

    Returns:
        ListParentsResponseTypeDef: _description_
    """

    parent_list: list[ListParentsResponseTypeDef] = []

    org_client = session.client(service_name="organizations")
    try:
        paginator: ListParentsPaginator = org_client.get_paginator("list_parents")

        for page in paginator.paginate(ChildId=child_id):
            for parent in page["Parents"]:
                parent_list.append(parent)

        return parent_list

    except (
        org_client.exceptions.AccessDeniedException,
        org_client.exceptions.AWSOrganizationsNotInUseException,
        org_client.exceptions.ChildNotFoundException,
        org_client.exceptions.InvalidInputException,
        org_client.exceptions.ServiceException,
        org_client.exceptions.TooManyRequestsException,
    ) as e:
        return str(object=e)


def create_ou_path_from_parent_ids(
    child_id: str, path_string: list[str], session: Session
) -> None:
    """_summary_"""
    # build the original ou structure with the root at the top and then all children
    # sit at the same secondary level but point to their children but also the parent
    # use this method to iterate through the data structure to build a full path until
    # the root is reached

    # if the child_id starts with "r-" then we have reached the root
    if child_id.startswith("r-"):
        return

    get_parent_id: ListParentsResponseTypeDef = list_parents(
        session=session, child_id=child_id
    )
    parent_id: str = get_parent_id[0]["Id"]

    # if the parent_id starts with "r-" then we have reached the root
    if parent_id.startswith("r-"):
        path_string.append("Root")
        return

    parent_details: DescribeOrganizationalUnitResponseTypeDef = describe_ou(
        session=session, ou_id=parent_id
    )
    parent_name: str = parent_details["OrganizationalUnit"]["Name"]
    path_string.append(parent_name)

    create_ou_path_from_parent_ids(
        child_id=parent_id, path_string=path_string, session=session
    )


def update_ou_structure(
    ou_structure: RootOrganizationalUnitBreakdownTypeDef,
    parent_id: str,
    session: Session,
) -> None:
    """updater function to create child objects

    Args:
        ou_structure (RootOrganizationalUnitBreakdownTypeDef): _description_
        parent_id (str): _description_
        session (Session): _description_
        ou_id (str): _description_
    """
    update_ou: Union[DescribeOrganizationalUnitResponseTypeDef, str] = describe_ou(
        session=session, ou_id=ou_structure["Id"]
    )
    update_accounts: Union[ListRootsResponseTypeDef, str] = list_children(
        session=session, parent_id=ou_structure["Id"], child_type="ACCOUNT"
    )
    update_children: Union[ListRootsResponseTypeDef, str] = list_children(
        session=session, parent_id=ou_structure["Id"], child_type="ORGANIZATIONAL_UNIT"
    )

    for account in update_accounts:
        update_accounts.remove(account)
        account_details: DescribeAccountResponseTypeDef = describe_account(
            session=session, account_id=account["Id"]
        )["Account"]
        account_details.update(
            {
                "JoinedTimestamp": account_details["JoinedTimestamp"].strftime(
                    "%Y-%m-%dT%H:%M:%S"
                )
            }
        )
        account_details.update({"Parent": update_ou["OrganizationalUnit"]["Name"]})
        path_list: list[str] = []
        create_ou_path_from_parent_ids(
            child_id=account["Id"], path_string=path_list, session=session
        )
        path: str = "/".join(list(reversed(path_list)))
        account_details.update({"Path": f"/{path}"})
        update_accounts.append(account_details)
        flattened_accounts.append(account_details)

    if update_children:
        for child in update_children:
            update_ou_structure(
                ou_structure=child, parent_id=child["Id"], session=session
            )

    if not update_accounts:
        update_accounts = "NULL"

    if not update_children:
        update_children = "NULL"

    ou_structure.update({"Parent": parent_id})
    ou_structure.update({"Name": update_ou["OrganizationalUnit"]["Name"]})
    ou_structure.update({"Arn": update_ou["OrganizationalUnit"]["Arn"]})
    ou_structure.update({"Accounts": update_accounts})
    ou_structure.update({"Children": update_children})


def create_aws_account_ds(parent_id: str, session: Session) -> dict[str, Any]:
    """Creates a parent child tree like data structure to
    record all roots and children in an AWS organization

    Args:
        parent_id (str): _description_
        session (Session): _description_

    Returns:
        dict[str, Any]: _description_
    """

    ou_roots: Union[ListRootsResponseTypeDef, str] = list_children(
        session=session,
        parent_id=parent_id,
        child_type="ORGANIZATIONAL_UNIT",
    )

    top_level_roots: list[RootTypeDef] = []

    thinker: str = ""
    for ou in ou_roots:
        thinker += "."
        print(f"Thinking in progress{thinker}", end="\r")
        ou_id = ou["Id"]

        if parent_id == "r-nyw4":
            update_ou_structure(ou_structure=ou, parent_id=parent_id, session=session)
            top_level_roots.append(ou)
            root_ou_breakdown.update({"Children": top_level_roots})

        create_aws_account_ds(parent_id=ou_id, session=session)


def main() -> None:
    """Execution of gathered logic"""

    # create session and connect to organizations client
    session = boto3.Session(profile_name="AdministratorAccess-160419733331")
    root_response: ListRootsResponseTypeDef = list_roots(session=session)["Roots"][0]

    # build root id inside of root_ou_breakdown
    root_arn = root_response["Arn"]
    root_id = root_response["Id"]
    root_name = root_response["Name"]

    root_ou_breakdown.update({"Arn": root_arn, "Id": root_id, "Name": root_name})

    create_aws_account_ds(
        parent_id=list_roots(session=session)["Roots"][0]["Id"], session=session
    )

    with open(file="ou_structure.json", mode="w", encoding="utf-8") as ou_structure:
        json.dump(obj=root_ou_breakdown, fp=ou_structure, indent=4)

    with open(file="accounts.json", mode="w", encoding="utf-8") as accounts:
        json.dump(obj=flattened_accounts, fp=accounts, indent=4)


if __name__ in ("__main__", "builtins", "__builtins__"):
    main()
