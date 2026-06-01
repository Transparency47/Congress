# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8471?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8471
- Title: PRIMATE Act
- Congress: 119
- Bill type: HR
- Bill number: 8471
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-13T08:06:47Z
- Update date including text: 2026-05-13T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8471",
    "number": "8471",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PRIMATE Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:47Z",
    "updateDateIncludingText": "2026-05-13T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:04:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "IN"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8471ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8471\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Steube (for himself, Ms. Titus , Ms. Malliotakis , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Tariff Act of 1930 to prohibit the importation on nonhuman primates.\n#### 1. Short title\nThis Act may be cited as the Preventing Risky Importation of Monkeys to Avoid Toxic Exposures Act or the PRIMATE Act .\n#### 2. Prohibition on importation of nonhuman primates\nTitle III of the Tariff Act of 1930 is amended by inserting after section 308 ( 19 U.S.C. 1308 ) the following:\n308A. Prohibition on importation of nonhuman primates (a) Definitions In this section\u2014 (1) the term AZA-accredited facility means a facility accredited by the Association of Zoos and Aquariums (AZA); (2) the term nonhuman primate means any live member of the taxonomic order Primates other than Homo sapiens; (3) the term person includes any individual, partnership, corporation, association, organization, business trust, government entity, or other entity subject to the jurisdiction of the United States; (4) the term Secretary means the Secretary of the Treasury; and (5) the term United States means the customs territory of the United States, as defined in general note 2 of the Harmonized Tariff Schedule of the United States. (b) Prohibition Notwithstanding any other provision of law, and except as provided in subsection (c), it shall be unlawful for any person to import into the United States any nonhuman primate. (c) Exception This section shall not apply to the importation of a nonhuman primate\u2014 (1) by, and for placement with, an AZA-accredited facility; and (2) with respect to which the importer certifies that the nonhuman primate will not be transferred, sold, leased, or otherwise provided for use in experiments or testing, or for breeding for use in experiments or testing. (d) Enforcement U.S. Customs and Border Protection shall deny clearance for any shipment for importation into the United States containing a nonhuman primate as prohibited by subsection (b). (e) Penalties (1) Civil penalties Any person who violates any provision of this section or any regulation issued under this section may, in addition to any other civil or criminal penalty that may be imposed under title 18, United States Code, or any other provision of law, be assessed a civil penalty by the Secretary of not more than $50,000 for each violation of this section. (2) Forfeiture Any nonhuman primate imported into the United States contrary to the provisions of this section or any regulation issued under this section shall be subject to forfeiture to the United States. (f) Regulations Not later than one year after the date of the enactment of this section, the Secretary shall, after notice and opportunity for comment, issue regulations to carry out the provisions of this section. .",
      "versionDate": "2026-04-23",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-05-06T20:40:01Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8471ih.xml"
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
      "title": "PRIMATE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T06:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PRIMATE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Risky Importation of Monkeys to Avoid Toxic Exposures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T06:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Tariff Act of 1930 to prohibit the importation on nonhuman primates.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T06:03:35Z"
    }
  ]
}
```
