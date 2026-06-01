# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3346?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3346
- Title: Freedom to Heal Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3346
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-02-12T12:03:24Z
- Update date including text: 2026-02-12T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3346",
    "number": "3346",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Freedom to Heal Act of 2025",
    "type": "S",
    "updateDate": "2026-02-12T12:03:24Z",
    "updateDateIncludingText": "2026-02-12T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
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
            "date": "2025-12-04T18:28:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-04T18:28:33Z",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "KY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3346is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3346\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Booker (for himself and Mr. Paul ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a special registration under the Controlled Substances Act for schedule I eligible investigational drugs under the Federal Right to Try law.\n#### 1. Short title\nThis Act may be cited as the Freedom to Heal Act of 2025 .\n#### 2. Special registration requirements related to right to try\nSection 303 of the Controlled Substances Act ( 21 U.S.C. 823 ) is amended by adding at the end the following:\n(p) Special registration for schedule I eligible investigational drugs under right to try (1) Definitions In this subsection, the terms eligible investigational drug and eligible patient have the meanings given those terms in section 561B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20130a ). (2) Special registration process The Attorney General shall register physicians to directly administer eligible investigational drugs in schedule I to eligible patients under section 561B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20130a ) in accordance with paragraphs (3) through (8) of this subsection. (3) Requirements (A) Application A physician desiring a registration to directly administer an eligible investigational drug as described in paragraph (2) shall submit to the Attorney General an application containing\u2014 (i) evidence of a valid registration to dispense or administer controlled substances in schedules II through V; (ii) evidence of compliance with section 561B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bbb\u20130a ), including\u2014 (I) documentation from the manufacturer or sponsor verifying the investigational drug in schedule I is an eligible investigational drug; (II) an agreement from the manufacturer or sponsor to supply the eligible investigational drug, along with guidance on its administration, to the requesting physician for the treatment of eligible patients; and (III) an affirmation that the physician will only directly administer the eligible investigational drug to treat eligible patients in a manner consistent with the guidance provided by the manufacturer or sponsor; (iii) the quantity of the eligible investigational drug to be supplied by the manufacturer or sponsor to the physician to treat eligible patients; (iv) evidence that the physician may treat eligible patients with eligible investigational drugs under the laws of the State in which the treatment will take place; (v) evidence of training, credentials, or experience relevant to treating patients with the eligible investigational drug; (vi) a description of the site at which the physician intends to store and administer the eligible investigational drug; and (vii) any additional information the Attorney General determines necessary to prevent diversion. (B) Approval Not later than 45 days after receiving an application containing the information required under subparagraph (A), the Attorney General shall\u2014 (i) register the applicant; or (ii) serve an order to show cause upon the applicant in accordance with section 304(c). (4) Electronic submissions The Attorney General shall provide a means for a physician to submit an application under paragraph (3)(A) electronically. (5) Limitation on amounts A physician treating eligible patients with an eligible investigational drug in schedule I under this subsection may only possess the amounts of the eligible investigational drug identified in\u2014 (A) the application submitted to the Attorney General under paragraph (3)(A); or (B) a supplemental notification that the physician may submit to the Attorney General if the physician needs additional amounts of the eligible investigational drug for the treatment of eligible patients, which supplemental notification\u2014 (i) shall include\u2014 (I) the name of the physician; (II) the additional quantity of the eligible investigational drug needed; and (III) an attestation that the treatment with the eligible investigational drug is consistent with the scope of treatment that was the subject of the application under paragraph (3)(A); and (ii) shall be deemed approved on the date that is 30 days after the date on which the physician submits the supplemental notification to the Attorney General, unless the Attorney General serves an order to show cause upon the applicant in accordance with section 304(c). (6) Single registration for related treatment sites A physician may treat eligible patients with an eligible investigational drug in schedule I under a single registration under this subsection if\u2014 (A) the treatment occurs exclusively on sites all of which are\u2014 (i) within the same city or county; and (ii) under the control of the same institution, organization, or agency; and (B) before commencing the treatment, the physician notifies the Attorney General of each site where the eligible investigational drug will be stored or administered in accordance with paragraph (3)(A)(vi). (7) Rulemaking Notwithstanding the requirements of section 553 of title 5, United States Code, not later than 240 days after the date of enactment of this subsection, the Attorney General shall issue an interim final rule to implement this subsection, including with respect to\u2014 (A) the manner in which an eligible investigational drug may be delivered to an approved registrant; (B) the storage and security of an eligible investigational drug; (C) the maintenance of records for an approved registrant; (D) the process for renewal, suspension, or revocation of a registration; and (E) any other matters necessary to ensure effective controls against diversion. (8) Final rule Not later than 2 years after issuing an interim final rule under paragraph (7), the Attorney General shall issue a final rule to implement this subsection in accordance with section 553 of title 5, United States Code. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6434",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Freedom to Heal Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-06T15:54:00Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3346is.xml"
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
      "title": "Freedom to Heal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom to Heal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a special registration under the Controlled Substances Act for schedule I eligible investigational drugs under the Federal Right to Try law.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:48:27Z"
    }
  ]
}
```
