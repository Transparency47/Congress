# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8544
- Title: PURE Executive Act
- Congress: 119
- Bill type: HR
- Bill number: 8544
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-19T19:47:34Z
- Update date including text: 2026-05-19T19:47:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8544",
    "number": "8544",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "PURE Executive Act",
    "type": "HR",
    "updateDate": "2026-05-19T19:47:34Z",
    "updateDateIncludingText": "2026-05-19T19:47:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8544ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8544\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mrs. Hinson (for herself and Mr. Golden of Maine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a 5-year post-employment ban on lobbying by former senior executive branch personnel and to prohibit such personnel from lobbying at any time on behalf of foreign governments or entities controlled by foreign governments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting the Unbiased Role of Employees in the Executive Act or the PURE Executive Act .\n#### 2. 5-year post-employment ban on lobbying by former senior executive branch personnel\n##### (a) 5-Year ban\nSection 207 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(1), by striking within 1 year after the termination and inserting within 5 years after the termination ; and\n**(2)**\nin subsection (d)(1), by striking within 2 years after the termination and inserting within 5 years after the termination .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to any individual who, on or after the date of the enactment of this Act, leaves a position to which subsection (c) or (d) of section 207 of title 18, United States Code, applies.\n#### 3. Lifetime ban on lobbying by former senior executive branch personnel on behalf of foreign governments or entities owned or controlled by foreign governments\n##### (a) Lifetime prohibition\nSection 207(f) of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraph (3) as paragraph (4); and\n**(2)**\nby inserting after paragraph (2) the following new paragraph:\n(3) Special rule for senior personnel of the executive branch and independent agencies In the case of an individual who is subject to the restrictions of subsection (c) or (d), the restrictions described in paragraph (1) shall apply to representing, aiding, or advising a foreign entity, or representing, aiding, or advising any entity which is subject to the direction, ownership, control, or influence of a foreign entity, at any time after the individual leaves a position to which such subsection applies. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to any individual who, on or after the date of the enactment of this Act, leaves a position to which subsection (c) or (d) of section 207 of title 18, United States Code, applies.",
      "versionDate": "2026-04-28",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-19T19:47:33Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8544ih.xml"
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
      "title": "PURE Executive Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PURE Executive Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting the Unbiased Role of Employees in the Executive Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish a 5-year post-employment ban on lobbying by former senior executive branch personnel and to prohibit such personnel from lobbying at any time on behalf of foreign governments or entities controlled by foreign governments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:37Z"
    }
  ]
}
```
