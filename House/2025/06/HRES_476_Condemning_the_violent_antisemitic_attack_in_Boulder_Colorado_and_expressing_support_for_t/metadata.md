# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/476
- Title: Condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.
- Congress: 119
- Bill type: HRES
- Bill number: 476
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-12-17T19:44:34Z
- Update date including text: 2025-12-17T19:44:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H2632)
- Latest action: 2025-06-04: Submitted in House

## Actions

- 2025-06-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-04 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Sponsor introductory remarks on measure. (CR H2632)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/476",
    "number": "476",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
    "type": "HRES",
    "updateDate": "2025-12-17T19:44:34Z",
    "updateDateIncludingText": "2025-12-17T19:44:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2632)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-04T14:06:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "CO"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NM"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "RI"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "OR"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres476ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 476\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Neguse (for himself, Ms. Pettersen , Ms. DeGette , Mr. Crow , Mr. Hurd of Colorado , and Mr. Crank ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCondemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.\nThat the House of Representatives\u2014\n**(1)**\ncondemns the antisemetic attack that occurred on June 1, 2025, in Boulder, Colorado;\n**(2)**\nexpresses solidarity with the survivors and their families;\n**(3)**\nrecognizes the resilience of the Boulder community and commends their continued efforts to promote peace, safety, and inclusion;\n**(4)**\ncalls for continued vigilance and Federal resources to counter rising antisemetism, investigate hate crimes, and support targeted communities;\n**(5)**\nstands with the Jewish community, for freedom of speech and religion, and against fear; and\n**(6)**\naffirms that hate and violence have no place in the United States, and that all people, regardless of faith or belief, deserve to live free from fear and persecution.",
      "versionDate": "2025-06-04",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-04",
        "text": "Referred to the Committee on the Judiciary. (text: CR S3236)"
      },
      "number": "263",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-12",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3396; text: CR S3394)"
      },
      "number": "278",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2025-07-22T19:38:08Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-22T19:38:08Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-22T19:38:08Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-07-22T19:38:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-18T12:59:05Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres476ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T08:18:19Z"
    },
    {
      "title": "Condemning the violent antisemitic attack in Boulder, Colorado, and expressing support for the survivors and their families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T08:06:59Z"
    }
  ]
}
```
