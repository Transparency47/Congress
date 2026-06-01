# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7181
- Title: Replacement Parts Availability Act
- Congress: 119
- Bill type: HR
- Bill number: 7181
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-02-10T16:19:05Z
- Update date including text: 2026-02-10T16:19:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7181",
    "number": "7181",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Replacement Parts Availability Act",
    "type": "HR",
    "updateDate": "2026-02-10T16:19:05Z",
    "updateDateIncludingText": "2026-02-10T16:19:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:02:40Z",
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
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7181ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7181\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Hudson (for himself and Mr. Balderson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Toxic Substances Control Act to clarify the exemption for replacement parts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Replacement Parts Availability Act .\n#### 2. Replacement parts\n##### (a) In general\nSection 6(c)(2)(D) of the Toxic Substances Control Act ( 15 U.S.C. 2605(c)(2)(D) ) is amended\u2014\n**(1)**\nby redesignating clause (ii) as clause (vi); and\n**(2)**\nin clause (i), to read as follows:\n(i) In general The Administrator shall exempt replacement parts for complex durable goods and complex consumer goods that are designed prior to the date of publication in the Federal Register of the rule under subsection (a). (ii) Exception The Administrator may only regulate replacement parts if the Administrator\u2014 (I) finds through the risk evaluation conducted under subsection (b)(4)(A) that such replacement parts contribute significantly to the risk to the general population or to an identified potentially exposed or susceptible subpopulation; and (II) makes an express written determination for such replacement parts, supported by substantial evidence in the risk evaluation, that the replacement part alone contributes significantly to the risk to the general population or to an identified potentially exposed or susceptible subpopulation. (iii) Clarification When replacement parts are excluded from a risk evaluation under subsection (b), any rule issued under subsection (a) shall constitute final agency action for the exclusion of replacement parts for complex durable goods or complex consumer goods that were designed prior to the date of publication of such rule. (iv) Upstream supply (I) The Administrator shall not prohibit the manufacture, processing, or import of a chemical substance to the extent that such chemical substance is necessary for the manufacture of replacement parts exempted under this section. (II) The Administrator shall establish procedures to ensure that such manufacture, processing, or import is limited exclusively to the manufacturer of replacement parts. (v) Transition period Any prohibition or restriction on replacement parts for complex durable goods permitted under this subparagraph shall allow for a transition period of not less than 10 years. .\n##### (b) Technical corrections\nSection 3 of the Toxic Substances Control Act ( 15 U.S.C. 2602 ) is amended:\n**(1)**\nIn paragraph (1), by striking the term and inserting The term ; and\n**(2)**\nIn paragraph 15(B)(i), by striking are and inserting is .",
      "versionDate": "2026-01-21",
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
        "name": "Environmental Protection",
        "updateDate": "2026-02-10T16:19:05Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7181ih.xml"
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
      "title": "Replacement Parts Availability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Replacement Parts Availability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Toxic Substances Control Act to clarify the exemption for replacement parts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T04:18:20Z"
    }
  ]
}
```
