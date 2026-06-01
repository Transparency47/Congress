# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6527
- Title: Justice for the Living Victims of Lockerbie Act
- Congress: 119
- Bill type: HR
- Bill number: 6527
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-14T08:07:29Z
- Update date including text: 2026-05-14T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6527",
    "number": "6527",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Justice for the Living Victims of Lockerbie Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:29Z",
    "updateDateIncludingText": "2026-05-14T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6527\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mrs. Kim (for herself and Ms. Lofgren ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide compensation for United States victims of Libyan State-sponsored terrorism, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for the Living Victims of Lockerbie Act .\n#### 2. Defined term\nIn this Act, the term compensable living victim of Libyan State-sponsored terrorism means an individual who\u2014\n**(1)**\nis a United States person;\n**(2)**\nwas 45 years of age or older on December 3, 1991;\n**(3)**\nwas employed by Pan American World Airways, Inc., on December 3, 1991;\n**(4)**\nwas a named claimant in Abbott et al. v. Socialist People\u2019s Libyan Arab Jamahiriya (case number 1:94\u2013cv\u201302444\u2013SS) in the United States District Court for the District of Columbia; and\n**(5)**\nwas alive on August 14, 2008.\n#### 3. Living Victims of Lockerbie Claims Trust Fund\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, the Secretary of the Treasury shall establish, in the Treasury of the United States, a trust fund, to be known as the Living Victims of Lockerbie Claims Trust Fund (in this section referred to as the Fund ) for the payment of claims submitted by compensable living victims of Libyan State-sponsored terrorism under section 4.\n##### (b) Appropriations\nOnce the Fund is established pursuant to subsection (a), there shall be appropriated to the Fund, out of any money in the Treasury of the United States not otherwise appropriated, $42,066,338, to remain available until expended, which shall be made available to provide compensation to compensable living victims of Libyan State-sponsored terrorism.\n#### 4. Compensation for living victims of Libyan State-sponsored terrorism\n##### (a) Certification by the Foreign Claims Settlement Commission\nThe Foreign Claims Settlement Commission shall\u2014\n**(1)**\nnot later than 30 days after the date of the enactment of this Act, publish in the Federal Register a notice of a process for filing claims on behalf of compensable living victims of Libyan State-sponsored terrorism, which shall include a deadline for the filing of claims of not later than the date that is 60 days after the date of publication of the notice;\n**(2)**\nnot later than 60 days after the end of the period for filing claims described in paragraph (1)\u2014\n**(A)**\ndetermine if each individual who submitted a claim under that paragraph is a compensable living victim of Libyan State-sponsored terrorism; and\n**(B)**\napprove the claim of each individual the Commission determines under subparagraph (A) to be a compensable living victim of Libyan State-sponsored terrorism; and\n**(3)**\nupon approving a claim under paragraph (2)(B), certify approval of the claim to the Secretary of the Treasury for purposes of authorization of payment under subsection (b).\n##### (b) Payments authorized\nUpon receiving a certification from the Foreign Claims Settlement Commission under subsection (a)(3), the Secretary of the Treasury shall make payments from the Fund to compensable living victims of Libyan State-sponsored terrorism in accordance with subsection (c).\n##### (c) Compensation\n**(1) In general**\nUpon a certification by the Foreign Claims Settlement Commission under subsection (a)(3) of the claim of a compensable living victim of Libyan State-sponsored terrorism, the claimant (or, in the case of a deceased claimant, the personal representative of the claimant\u2019s estate) shall be entitled to an award in an amount equal to\u2014\n**(A)**\n$42,066,338, divided by\n**(B)**\nthe total number of claims certified under subsection (a)(3).\n**(2) Representative**\nIf a putative claimant that otherwise qualifies for compensation under this section is deceased, a personal representative may bring a claim on behalf of the estate of the claimant.",
      "versionDate": "2025-12-09",
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T21:49:56Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6527ih.xml"
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
      "title": "Justice for the Living Victims of Lockerbie Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for the Living Victims of Lockerbie Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide compensation for United States victims of Libyan State-sponsored terrorism, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:30Z"
    }
  ]
}
```
