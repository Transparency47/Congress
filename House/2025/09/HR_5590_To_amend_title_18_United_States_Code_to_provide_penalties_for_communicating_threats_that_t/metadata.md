# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5590?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5590
- Title: SWAT Act
- Congress: 119
- Bill type: HR
- Bill number: 5590
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-11-18T18:19:46Z
- Update date including text: 2025-11-18T18:19:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5590",
    "number": "5590",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "SWAT Act",
    "type": "HR",
    "updateDate": "2025-11-18T18:19:46Z",
    "updateDateIncludingText": "2025-11-18T18:19:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:01:00Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5590ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5590\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Lawler (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide penalties for communicating threats that target schools.\n#### 1. Short title\nThis Act may be cited as the Schools Want Accountability for Threats Act or the SWAT Act .\n#### 2. Threats involving fire or explosives\nSection 844(e) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking (e) and inserting (e)(1) ; and\n**(2)**\nby adding at the end the following:\n(2) Whoever violates paragraph (1) by making a threat against, or maliciously conveying false information with respect to, a public, private, or religious school that provides early childhood, elementary, secondary, postsecondary, or career and technical education, as determined under State law, shall be imprisoned for not more than 20 years or fined under this title, or both. .\n#### 3. Threats through the mail or interstate communications\nChapter 41 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 875 by adding at the end the following:\n(e) Whoever violates any other provision of this section by making a threat against a public, private, or religious school that provides early childhood, elementary, secondary, postsecondary, or career and technical education, as determined under State law, shall be imprisoned for not more than 20 years or fined under this title, or both. ; and\n**(2)**\nin section 876 by adding at the end the following:\n(e) Whoever violates any other provision of this section by making a threat against a public, private, or religious school that provides early childhood, elementary, secondary, postsecondary, or career and technical education, as determined under State law, shall be imprisoned for not more than 20 years or fined under this title, or both. .\n#### 4. False information and hoaxes\nSection 1038(a)(1) of title 18, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B) by striking and ;\n**(2)**\nin subparagraph (C) by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(D) if the information indicates that the activity has taken, is taking, or will take place in a public, private, or religious school that provides early childhood, elementary, secondary, postsecondary, or career and technical education, as determined under State law, be fined under this title or imprisoned not more than 20 years, or both. .",
      "versionDate": "2025-09-26",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-18T18:19:46Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5590ih.xml"
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
      "title": "SWAT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SWAT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Schools Want Accountability for Threats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to provide penalties for communicating threats that target schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T10:18:14Z"
    }
  ]
}
```
