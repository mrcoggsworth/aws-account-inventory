# AWS-Account-Inventory

<br></br>

## Description

This repository is a dedicated area to develop code that collects AWS Organizations data that is gathered all the way from the Root to each account that exists.

### Example returns

---

- All examples here and in their respective files have been modified to not send sensitive details

accounts.json output

```json
[
    {
        "Id": "160411112222",
        "Arn": "arn:aws:organizations::160411112222:account/o-yyryk37ajh/160411112222",
        "Email": "christopher.scogin@redacted.dev",
        "Name": "scogin-dev",
        "Status": "ACTIVE",
        "JoinedMethod": "INVITED",
        "JoinedTimestamp": "2023-06-07T16:56:10",
        "Parent": "sogin-dev-sandbox",
        "Path": "/Root/core/sogin-dev-sandbox"
    },
    {
        "Id": "160511112222",
        "Arn": "arn:aws:organizations::160511112222:account/o-yyryk37ajh/160511112222",
        "Email": "cscogin@redacted.me",
        "Name": "guardrails-development",
        "Status": "ACTIVE",
        "JoinedMethod": "CREATED",
        "JoinedTimestamp": "2023-11-18T10:58:36",
        "Parent": "gr-dev",
        "Path": "/Root/core/gr-dev"
    }
]
```

ou_structure.json output

```json
{
    "Arn": "arn:aws:organizations::160411112222:root/o-yyryk37ajh/r-nyz5",
    "Id": "r-nyz5",
    "Name": "Root",
    "Children": [
        {
            "Id": "ou-nyw4-ju89em4s",
            "Type": "ORGANIZATIONAL_UNIT",
            "Parent": "r-nyz5",
            "Name": "decommissioned",
            "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-ju89em4s",
            "Accounts": "NULL",
            "Children": "NULL"
        },
        {
            "Id": "ou-nyw4-vcozez9j",
            "Type": "ORGANIZATIONAL_UNIT",
            "Parent": "r-nyz5",
            "Name": "quarantine",
            "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-vcozez9j",
            "Accounts": "NULL",
            "Children": "NULL"
        },
        {
            "Id": "ou-nyw4-rdsr1bvl",
            "Type": "ORGANIZATIONAL_UNIT",
            "Parent": "r-nyz5",
            "Name": "core",
            "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-rdsr1bvl",
            "Accounts": "NULL",
            "Children": [
                {
                    "Id": "ou-nyw4-245vwcoa",
                    "Type": "ORGANIZATIONAL_UNIT",
                    "Parent": "ou-nyw4-245vwcoa",
                    "Name": "sogin-dev-sandbox",
                    "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-245vwcoa",
                    "Accounts": [
                        {
                            "Id": "160411112222",
                            "Arn": "arn:aws:organizations::160411112222:account/o-yyryk37ajh/160411112222",
                            "Email": "christopher.scogin@redacted.dev",
                            "Name": "scogin-dev",
                            "Status": "ACTIVE",
                            "JoinedMethod": "INVITED",
                            "JoinedTimestamp": "2023-06-07T16:56:10",
                            "Parent": "sogin-dev-sandbox",
                            "Path": "/Root/core/sogin-dev-sandbox"
                        }
                    ],
                    "Children": "NULL"
                },
                {
                    "Id": "ou-nyw4-h6qjvp9i",
                    "Type": "ORGANIZATIONAL_UNIT",
                    "Parent": "ou-nyw4-h6qjvp9i",
                    "Name": "gr-dev",
                    "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-h6qjvp9i",
                    "Accounts": [
                        {
                            "Id": "160511112222",
                            "Arn": "arn:aws:organizations::160511112222:account/o-yyryk37ajh/160511112222",
                            "Email": "cscogin@redacted.me",
                            "Name": "guardrails-development",
                            "Status": "ACTIVE",
                            "JoinedMethod": "CREATED",
                            "JoinedTimestamp": "2023-11-18T10:58:36",
                            "Parent": "gr-dev",
                            "Path": "/Root/core/gr-dev"
                        }
                    ],
                    "Children": "NULL"
                },
                {
                    "Id": "ou-nyw4-vnviliyu",
                    "Type": "ORGANIZATIONAL_UNIT",
                    "Parent": "ou-nyw4-vnviliyu",
                    "Name": "eks-testing",
                    "Arn": "arn:aws:organizations::160411112222:ou/o-yyryk37ajh/ou-nyw4-vnviliyu",
                    "Accounts": "NULL",
                    "Children": "NULL"
                }
            ]
        }
    ]
}
```

### Future Enhancements

---

- Create cli tool to encompass commands
- Continue to add depth of data enrichement
 