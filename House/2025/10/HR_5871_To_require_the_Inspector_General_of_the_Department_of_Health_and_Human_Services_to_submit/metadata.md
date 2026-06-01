# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5871
- Title: We Want Our Healthcare Money Back Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5871
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-11-25T17:00:47Z
- Update date including text: 2025-11-25T17:00:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5871",
    "number": "5871",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "We Want Our Healthcare Money Back Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-25T17:00:47Z",
    "updateDateIncludingText": "2025-11-25T17:00:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-31T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5871ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5871\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Bean of Florida (for himself and Mr. Haridopolos ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Inspector General of the Department of Health and Human Services to submit a report on Medicare and Medicaid fraud.\n#### 1. Short title\nThis Act may be cited as the We Want Our Healthcare Money Back Act of 2025 .\n#### 2. Report on Medicare and Medicaid fraud\n##### (a) Report\nNot later than 3 months after the date of the enactment of this Act, and not less frequently than every 3 months thereafter until the date that is 2 years after the date of the enactment of this Act, the Inspector General of the Department of Health and Human Services (in this section referred to as the Inspector General ) shall submit a report on Medicare and Medicaid fraud, including the information described in subsection (b), to the following committees:\n**(1)**\nThe Committee on Ways and Means of the House of Representatives.\n**(2)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(3)**\nThe Committee on Finance of the Senate.\n**(4)**\nThe Committee on Health, Education, Labor, and Pensions of the Senate.\n##### (b) Information described\nFor purposes of subsection (a), the information described in this subsection is, with respect to the 3-month period ending on the date that is 1 month before the date on which the report under such subsection is required to be submitted\u2014\n**(1)**\nthe number of investigations of Medicare and Medicaid fraud conducted by the Inspector General during such period;\n**(2)**\nthe number of criminal prosecutions and civil actions alleging Medicare and Medicaid fraud commenced during such period as a result of an investigation conducted by the Inspector General;\n**(3)**\nthe dollar amount of fraud alleged in each such criminal prosecution and civil action;\n**(4)**\nthe charges alleged in each such criminal prosecution and civil action; and\n**(5)**\nthe number of individuals and entities excluded from participating in any Federal health care program (as such term is defined in section 1128B of the Social Security Act ( 42 U.S.C. 1320a\u20137b )) during such period due to a criminal conviction or other act related to Medicare and Medicaid fraud.\n##### (c) Medicare and Medicaid fraud defined\nIn this section, the term Medicare and Medicaid fraud means fraud related to the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) or the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1306 et seq. ).\n##### (d) No additional funds authorized\nNo additional amounts are authorized to be appropriated to carry out this section, and this section shall be carried out using amounts otherwise appropriated to the Secretary of Health and Human Services or the Inspector General of the Department of Health and Human Services.",
      "versionDate": "2025-10-31",
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
        "name": "Health",
        "updateDate": "2025-11-25T17:00:47Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5871ih.xml"
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
      "title": "We Want Our Healthcare Money Back Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T08:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "We Want Our Healthcare Money Back Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T08:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Inspector General of the Department of Health and Human Services to submit a report on Medicare and Medicaid fraud.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T08:33:21Z"
    }
  ]
}
```
