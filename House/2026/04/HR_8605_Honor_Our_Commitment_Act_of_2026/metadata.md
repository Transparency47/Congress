# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8605
- Title: Honor Our Commitment Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8605
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T21:50:09Z
- Update date including text: 2026-05-19T21:50:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8605",
    "number": "8605",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Honor Our Commitment Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T21:50:09Z",
    "updateDateIncludingText": "2026-05-19T21:50:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:06:40Z",
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
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8605ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8605\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Correa (for himself, Mr. Tran , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo halt removal of certain nationals of Vietnam, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honor Our Commitment Act of 2026 .\n#### 2. Limitation on the detention and removal of nationals of Vietnam\n##### (a) Limitation on detention and removal\nExcept as provided in subsection (b), an alien may not be detained or removed from the United States on or after the date of enactment of this Act if the alien\u2014\n**(1)**\nis a national of Vietnam;\n**(2)**\nentered the United States on or before July 12, 1995, and has continuously resided in the United States since such entry; and\n**(3)**\nis subject to a final order of removal.\n##### (b) Exception\nSubsection (a) shall not apply to an alien if\u2014\n**(1)**\nthe Secretary of Homeland Security determines, based on credible facts, that the alien is directly responsible for harming the security of the United States; or\n**(2)**\nthe alien is subject to extradition.\n##### (c) Employment authorization\nThe Secretary of Homeland Security shall authorize an alien described in subsection (a) to engage in employment in the United States and provide such alien with an employment authorized endorsement or other appropriate work permit.\n#### 3. Notice for certain Vietnamese nationals with removal orders\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the Secretary of Homeland Security shall provide notice of the provisions of this Act to each alien described in section 2(a).\n##### (b) Contents of notice\nThe notice described in subsection (a) shall include information explaining the requirements and instructions for filing a motion to reopen removal proceedings under section 240(c)(7) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(c)(7) ).\n#### 4. Judicial review\n##### (a) Review\nNotwithstanding any other provision of law, an individual or entity who has been harmed by a violation of this Act may file an action in an appropriate district court of the United States to seek declaratory or injunctive relief.\n##### (b) Rule of construction\nNothing in this Act may be construed to preclude an action filed pursuant to subsection (a) from proceeding as a class action (as such term is defined in section 1711 of title 28, United States Code).",
      "versionDate": "2026-04-30",
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
        "name": "Immigration",
        "updateDate": "2026-05-19T21:50:08Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8605ih.xml"
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
      "title": "Honor Our Commitment Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honor Our Commitment Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To halt removal of certain nationals of Vietnam, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:35Z"
    }
  ]
}
```
