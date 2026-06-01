# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/907
- Title: Ensuring Justice for Camp Lejeune Victims Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 907
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/907",
    "number": "907",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Ensuring Justice for Camp Lejeune Victims Act of 2025",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-03-06T21:14:48Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-06T21:14:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AR"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "ID"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s907is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 907\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Tillis (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Camp Lejeune Justice Act of 2022 to make technical corrections.\n#### 1. Short title\nThis Act may be cited as the Ensuring Justice for Camp Lejeune Victims Act of 2025 .\n#### 2. Technical corrections to the Camp Lejeune Justice Act of 2022\nSection 804 of the Camp Lejeune Justice Act of 2022 ( 28 U.S.C. 2671 note prec.) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby striking in the United States District Court for the Eastern District of North Carolina ; and\n**(B)**\nby inserting , including a latent or potential harm, after appropriate relief for harm ;\n**(2)**\nby amending subsection (c) to read as follows:\n(c) Burdens and standard of proof (1) In general The party filing an action under this section shall be entitled to appropriate relief upon showing\u2014 (A) the existence of 1 or more relationships between the type of contaminant in any water at Camp Lejeune and the type of harm suffered by the individual, including latent or potential harm; and (B) that the individual was present at Camp Lejeune for a period of not less than 30 days, whether or not consecutive. (2) Evidentiary standards To meet the burden of proof described in paragraph (1), a party shall produce evidence showing that the relationship between exposure to any level of contaminants of a type in any water at Camp Lejeune and the type of harm is\u2014 (A) sufficient to conclude that a causal relationship exists; or (B) sufficient to conclude that a causal relationship is at least as likely as not. ;\n**(3)**\nby amending subsection (d) to read as follows:\n(d) Exclusive jurisdiction and venue (1) In general The United States District Court for the Eastern District of North Carolina shall have exclusive jurisdiction and venue for coordinated or consolidated pretrial administrative and procedural matters and resolution over any action filed under subsection (b). (2) Transfer A party filing an action under subsection (b) may transfer such action to any district court of the United States situated within the fourth judicial circuit for pretrial and trial of such action, including the adjudication of all evidentiary motions. (3) Jury trial Any action against the United States under subsection (b) shall, at the request of either party to such action, be tried by the court with a jury. (4) Expedited disposition The court shall advance an action filed under subsection (b) on the docket, and expedite the disposition of such action to the greatest extent possible. ;\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), by striking latent disease and inserting latent or potential harm ; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Health and disability benefits relating to water exposure (A) Claims settled before filing An award to an individual, or legal representative of an individual, under this section that is made pursuant to a settlement entered before a civil action under subsection (b) is commenced shall not be offset. (B) Claims resolved after filing An award to an individual, or legal representative of an individual, under this section that is made pursuant to a settlement entered or judgment rendered after a civil action under subsection (b) is commenced shall be offset to the extent permitted by applicable law by the amount of any disability award, payment, or benefit provided to the individual, or legal representative\u2014 (i) under\u2014 (I) any program under the laws administered by the Secretary of Veterans Affairs; (II) the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ); or (III) the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ); and (ii) in connection with health care or a disability relating to exposure to the water at Camp Lejeune. ; and\n**(5)**\nby adding at the end the following:\n(k) Attorney fees (1) In general The total amount of attorneys fees under this section shall be in an amount that is not more than\u2014 (A) 20 percent of any settlement entered into before a civil action under subsection (b) is commenced; or (B) 25 percent of any judgement rendered or settlement entered into after a civil action under subsection (b) is commenced. (2) Division of fees A division of a fee under paragraph (1) between attorneys who are not in the same firm may be made only if the division is in proportion to the services performed by each attorney. (3) Rule of construction Nothing in this subsection shall prohibit an individual or the legal representative of an individual and such individual\u2019s or representative\u2019s attorney from agreeing to a fee award that is less than the maximum percentage specified in paragraph (1). .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect as if enacted on August 10, 2022, and shall apply to any claim or action under section 804 of the Camp Lejeune Justice Act of 2022 that is pending on, or filed on or after, the date of enactment of this Act.\n#### 4. Rule of construction\nNothing in this Act or an amendment made by this Act shall be construed to modify the applicability or statute of limitations provisions under section 804(j) of the Camp Lejeune Justice Act of 2022 ( 28 U.S.C. 2671 note prec.).",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4145",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Justice for Camp Lejeune Victims Act of 2025",
      "type": "HR"
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
        "name": "Law",
        "updateDate": "2025-03-28T13:09:27Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s907is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Ensuring Justice for Camp Lejeune Victims Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Justice for Camp Lejeune Victims Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Camp Lejeune Justice Act of 2022 to make technical corrections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:03:19Z"
    }
  ]
}
```
