# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8353
- Title: FAITH Act
- Congress: 119
- Bill type: HR
- Bill number: 8353
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-30T20:11:38Z
- Update date including text: 2026-04-30T20:11:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8353",
    "number": "8353",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "FAITH Act",
    "type": "HR",
    "updateDate": "2026-04-30T20:11:38Z",
    "updateDateIncludingText": "2026-04-30T20:11:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:04:05Z",
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
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8353ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8353\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Self introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a prohibition on fees related to religious participation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom Against Imposed Theology Harms Act or the FAITH Act .\n#### 2. Prohibition on fees related to religious participation\n##### (a) In general\nChapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Prohibition on fees related to religious participation (a) Offense Whoever knowingly imposes, assesses, collects, or attempts to impose, assess, or collect any fee, fine, surcharge, penalty, or other financial obligation from any person based on that person\u2019s participation or membership in, or refusal to participate in or become a member of, any religious theology, denomination, or organization shall\u2014 (1) in the case that the fee, fine, surcharge, penalty or other financial obligation does not exceed $1,000, shall be fined under this title, imprisoned not more than 1 year, or both; or (2) in any other case, shall be fined under this title, imprisoned not more than 3 years, or both. (b) Prohibiting denial of goods and services Whoever knowingly denies goods, services, access, or opportunities to a person on the basis of nonpayment of any fee prohibited under subsection (a) shall be fined under this title, imprisoned not more than 1 year, or both. (c) Rule of construction Nothing in this section shall be construed to restrict the ability of religious organizations and educational institutions to request or receive voluntary contributions from their members for internal purposes. .\n##### (b) Clerical amendment\nThe table of sections for chapter 13 of title 18, United States Code, is amended by adding at the end the following:\n251. Prohibition on fees related to religious participation. .\n#### 3. RICO offense\nSection 1961(1) of title 18, United States Code, is amended by inserting section 251 (relating to the prohibition on fees tied to religious participation), after section 224 (relating to sports bribery), .\n#### 4. Effective date\nThis Act and the amendments made by this Act shall take effect 30 days after the date of enactment of this Act.",
      "versionDate": "2026-04-16",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-04-30T20:11:38Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8353ih.xml"
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
      "title": "FAITH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAITH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom Against Imposed Theology Harms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a prohibition on fees related to religious participation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:31Z"
    }
  ]
}
```
