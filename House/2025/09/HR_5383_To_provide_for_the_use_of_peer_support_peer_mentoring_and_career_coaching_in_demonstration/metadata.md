# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5383?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5383
- Title: Mentoring and Supporting Families Act
- Congress: 119
- Bill type: HR
- Bill number: 5383
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-09-26T14:54:51Z
- Update date including text: 2025-09-26T14:54:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5383",
    "number": "5383",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Mentoring and Supporting Families Act",
    "type": "HR",
    "updateDate": "2025-09-26T14:54:51Z",
    "updateDateIncludingText": "2025-09-26T14:54:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:00:20Z",
          "name": "Referred To"
        }
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5383ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5383\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Evans of Pennsylvania introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide for the use of peer support, peer mentoring, and career coaching in demonstration projects conducted under the health profession opportunity grant program under section 2008 of the Social Security Act.\n#### 1. Short title\nThis Act may be cited as the Mentoring and Supporting Families Act .\n#### 2. Use of peer support, peer mentoring, and career coaching\nSection 2008 of the Social Security Act ( 42 U.S.C. 1397g ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Use of peer support, peer mentoring, and career coaching (1) Preference in considering applications In considering applications for a grant under this section, the Secretary shall give preference to\u2014 (A) applications that include opportunities for mentoring or peer support, and make career coaching available, as part of the case management plan; and (B) applications that include a commitment to providing project participants with a monthly cash stipend or wage supplement. (2) Inclusion among support services A project for which a grant is made under this section shall include case management plans that include career coaching (with the option to offer appropriate peer support and mentoring opportunities to help develop soft skills and social capital), which may be offered on an ongoing basis before, during, and after initial training as part of a career pathway model. .\n#### 3. Effective date\nThe amendment made by this Act shall take effect on October 1, 2025.",
      "versionDate": "2025-09-16",
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
        "updateDate": "2025-09-26T14:54:51Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5383ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the use of peer support, peer mentoring, and career coaching in demonstration projects conducted under the health profession opportunity grant program under section 2008 of the Social Security Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:47Z"
    },
    {
      "title": "Mentoring and Supporting Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mentoring and Supporting Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
