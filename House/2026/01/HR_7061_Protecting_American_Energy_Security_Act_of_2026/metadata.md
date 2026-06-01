# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7061?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7061
- Title: Protecting American Energy Security Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7061
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-03-09T17:23:22Z
- Update date including text: 2026-03-09T17:23:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7061",
    "number": "7061",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "E000301",
        "district": "3",
        "firstName": "Sarah",
        "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
        "lastName": "Elfreth",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Protecting American Energy Security Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-09T17:23:22Z",
    "updateDateIncludingText": "2026-03-09T17:23:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:00:05Z",
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7061ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7061\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Ms. Elfreth (for herself, Ms. Castor of Florida , Ms. Salazar , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Natural Gas Act to require that a certification issued by the Secretary of Energy be in effect in order to export natural gas to a covered nation.\n#### 1. Short title\nThis Act may be cited as the Protecting American Energy Security Act of 2026 .\n#### 2. Certification required for exports of natural gas to covered nations\nSection 3 of the Natural Gas Act ( 15 U.S.C. 717b ) is amended by adding at the end the following:\n(g) Certification required for certain exports No person shall export any natural gas from the United States to a covered nation (as such term is defined in section 4872(f) of title 10, United States Code) without having in effect, in addition to an order authorizing such export issued under subsection (a), a certification issued by the Secretary of Energy that such export would be in the public interest. Upon issuance, such a certification shall be in effect for a period of one year unless the Secretary of Energy revokes the certification prior to the conclusion of such period. .",
      "versionDate": "2026-01-14",
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
        "name": "Energy",
        "updateDate": "2026-03-09T17:23:21Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7061ih.xml"
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
      "title": "Protecting American Energy Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting American Energy Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Natural Gas Act to require that a certification issued by the Secretary of Energy be in effect in order to export natural gas to a covered nation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T05:18:29Z"
    }
  ]
}
```
