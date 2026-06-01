# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7141
- Title: Affordable Housing Guarantee Act
- Congress: 119
- Bill type: HR
- Bill number: 7141
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-02-25T09:06:23Z
- Update date including text: 2026-02-25T09:06:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-16 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-16 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-02-24 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-24 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7141",
    "number": "7141",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Affordable Housing Guarantee Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:23Z",
    "updateDateIncludingText": "2026-02-25T09:06:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-01-16T20:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-24T22:39:45Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-24T22:39:35Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-16T22:37:29Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7141ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7141\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to modify the maximum guaranty amount of certain home loans guaranteed by the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Affordable Housing Guarantee Act .\n#### 2. Maximum guaranty amount of certain home loans guaranteed by the Department of Veterans Affairs\nSection 3703(a)(1)(A)(i)(IV) of title 38, United States Code, is amended\u2014\n**(1)**\nby striking title, 25 percent of the loan; or and inserting title\u2014 ; and\n**(2)**\nby adding at the end the following new items:\n(aa) in the case of a veteran with a service-connected disability whose entitlement under this chapter is unused or has been restored in full, 50 percent of the loan; and (bb) in the case of a veteran other than a veteran described in item (aa), 25 percent of the loan; or .",
      "versionDate": "2026-01-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-09T19:18:55Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7141ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Affordable Housing Guarantee Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Housing Guarantee Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to modify the maximum guaranty amount of certain home loans guaranteed by the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:35Z"
    }
  ]
}
```
