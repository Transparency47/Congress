# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8884?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8884
- Title: Removing Barriers to Work for Disabled Americans Act
- Congress: 119
- Bill type: HR
- Bill number: 8884
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-22T08:07:56Z
- Update date including text: 2026-05-22T08:07:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8884",
    "number": "8884",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001189",
        "district": "8",
        "firstName": "Austin",
        "fullName": "Rep. Scott, Austin [R-GA-8]",
        "lastName": "Scott",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Removing Barriers to Work for Disabled Americans Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:56Z",
    "updateDateIncludingText": "2026-05-22T08:07:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 27 - 16.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
        "item": [
          {
            "date": "2026-05-21T15:10:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:04:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8884ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8884\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Austin Scott of Georgia introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to reauthorize demonstration authority for the disability insurance program.\n#### 1. Short title\nThis Act may be cited as the Removing Barriers to Work for Disabled Americans Act .\n#### 2. Temporary reauthorization of disability insurance demonstration project authority\n##### (a) Termination date\nSection 234(d)(2) of the Social Security Act ( 42 U.S.C. 434(d)(2) ) is amended by striking December 31, 2021, and the authority to carry out such projects shall terminate on December 31, 2022 and inserting December 31, 2030, and the authority to carry out such projects shall terminate on December 31, 2031 .\n##### (b) Authority To waive compliance with benefits requirements\nSection 234(c) of such Act is amended\u2014\n**(1)**\nby striking December 30, 2021 and inserting December 31, 2030 ;\n**(2)**\nby striking 90 days and inserting 120 days ; and\n**(3)**\nby inserting after the expected annual and total costs, the following: evaluation metrics to be used with respect to the experiment or demonstration project, .\n##### (c) Expenditure\nSection 201(k) of such Act ( 42 U.S.C. 401(k) ) is amended to read as follows:\n(k) Administrative expenditures for experiments and demonstration projects under section 234 shall be paid from funds made available for the administration of this title. Benefits payable to or on behalf of individuals by reason of participation in experiments and demonstration projects under section 234 shall be made from the Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund, as determined appropriate by the Commissioner of Social Security. .\n##### (d) Limitation\nSection 234(e) of the Social Security Act ( 42 U.S.C. 434(e) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking the and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) that the total income of an individual will not be reduced due to the individual\u2019s participation in an experiment or demonstration project. .\n##### (e) Technical amendment\nSection 234 of such Act ( 42 U.S.C. 434 ) is further amended by striking subsection (f).\n##### (f) Effective date\nThe amendments made by this section shall take effect on January 1, 2027.",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8884ih.xml"
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
      "title": "Removing Barriers to Work for Disabled Americans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Removing Barriers to Work for Disabled Americans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to reauthorize demonstration authority for the disability insurance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:38Z"
    }
  ]
}
```
