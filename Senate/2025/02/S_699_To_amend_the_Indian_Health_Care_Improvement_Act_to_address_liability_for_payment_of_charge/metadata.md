# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/699
- Title: Purchased and Referred Care Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 699
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2026-04-29T11:03:31Z
- Update date including text: 2026-04-29T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/699",
    "number": "699",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Purchased and Referred Care Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:31Z",
    "updateDateIncludingText": "2026-04-29T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-24",
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
            "date": "2026-02-04T19:15:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-24T23:53:29Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "WA"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "SD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "WA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "ND"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s699is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 699\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. Rounds (for himself, Ms. Cantwell , Mr. Thune , and Mrs. Murray ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo amend the Indian Health Care Improvement Act to address liability for payment of charges or costs associated with the provision of purchased/referred care services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Purchased and Referred Care Improvement Act of 2025 .\n#### 2. Changes to liability for payment\n##### (a) In general\nSection 222 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621u ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking A patient who receives contract health care services and inserting Notwithstanding any other provision of law or any agreement, form, or other written or electronic document signed by a patient, a patient who receives purchased/referred care ; and\n**(B)**\nby striking such services and inserting the purchased/referred care ;\n**(2)**\nby striking subsection (b) and inserting the following:\n(b) Notification The Secretary shall notify a purchased/referred care provider and any patient who receives purchased/referred care authorized by the Service that, notwithstanding any other provision of law or any agreement, form, or other written or electronic document signed by the patient, the patient is not liable to any provider, debt collector, or any other person for the payment of any charges or costs associated with the provision of the purchased/referred care not later than 5 business days after receipt of a notification of a claim by a provider of the purchased/referred care. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby inserting , debt collector, or any other person, as applicable, after the provider ; and\n**(B)**\nby striking the services and inserting the purchased/referred care ; and\n**(4)**\nby adding at the end the following:\n(d) Reimbursement (1) Establishment of procedures (A) In general Not later than 120 days after the date of enactment of the Purchased and Referred Care Improvement Act of 2025 , in consultation with Indian tribes, and except as provided in paragraph (2), the Secretary shall establish and implement procedures to allow a patient that paid out-of-pocket for purchased/referred care authorized by the Service under this Act to be reimbursed by the Service for that payment not later than 30 days after the date on which the patient submits documentation to the Service in accordance with subparagraph (B). (B) Submitting documentation The Secretary shall accept documentation from a patient seeking reimbursement under paragraph (1) that was submitted\u2014 (i) electronically; or (ii) in-person at a Service facility. (2) Limitation Paragraph (1) shall not apply to purchased/referred care furnished under a purchased/referred care services program operated by an Indian tribe under a contract or compact entered into under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ) unless expressly agreed to by the Indian tribe. (e) Updating authorities Not later than 180 days after the date of enactment of the Purchased and Referred Care Improvement Act of 2025 , the Secretary, in consultation with Indian tribes, shall update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of this section. .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to purchased/referred care (as defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )) authorized by the Indian Health Service furnished on, before, or after the date of enactment of this Act.\n#### 3. Technical and conforming amendments\n##### (a) Definitions\nSection 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ) is amended\u2014\n**(1)**\nby striking paragraph (5);\n**(2)**\nby redesignating paragraphs (6) through (15) as paragraph (5) through (14), respectively;\n**(3)**\nin paragraph (12) (as so redesignated), in the matter preceding subparagraph (A), by striking , as defined in subsection (d) hereof, ;\n**(4)**\nby inserting after paragraph (14) (as so redesignated) the following:\n(15) Purchased/referred care The term purchased/referred care means any health service that is\u2014 (A) delivered based on a referral by, or at the expense of, an Indian health program; and (B) provided by a public or private medical provider or hospital that is not a provider or hospital of the Indian health program. ;\n**(5)**\nin paragraph (25), by striking ( 25 U.S.C. 450 et seq. ) and inserting ( 25 U.S.C. 5301 et seq. ) ;\n**(6)**\nin paragraph (26), by striking ( 25 U.S.C. 450b ) and inserting ( 25 U.S.C. 5304 ) ; and\n**(7)**\nin paragraph (28)\u2014\n**(A)**\nby striking , as defined in subsection (g) hereof, ; and\n**(B)**\nby striking subsection (c)(1) through (4) of this section and inserting subparagraphs (A) through (D) of paragraph (12) .\n##### (b) Technical and conforming amendments\n**(1)**\nThe Indian Health Care Improvement Act ( 25 U.S.C. 1601 et seq. ) is amended\u2014\n**(A)**\nby striking contract health service each place it appears and inserting purchased/referred care ;\n**(B)**\nby striking contract health services each place it appears and inserting purchased/referred care ;\n**(C)**\nby striking Contract Health Service each place it appears and inserting purchased/referred care ;\n**(D)**\nby striking Contract Health Services each place it appears and inserting purchased/referred care ; and\n**(E)**\nby striking contract care each place it appears and inserting purchased/referred care .\n**(2)**\nSection 211 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621j ) is amended by striking the section heading and designation and all that follows through (a) The Secretary and inserting the following:\n211. California purchased/referred care demonstration program (a) The Secretary .\n**(3)**\nSection 219 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621r ) is amended by striking the section heading and designation and all that follows through (a) The Secretary and inserting the following:\n219. Purchased/referred care payment study (a) The Secretary .\n**(4)**\nSection 226 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621y ) is amended, in the section heading, by striking Contract health service and inserting Purchased/referred care .\n**(5)**\nSection 406 of the Indian Health Care Improvement Act ( 25 U.S.C. 1646 ) is amended by striking the section heading and designation and all that follows through With respect and inserting the following:\n406. Authorization for emergency purchased/referred care With respect .\n**(6)**\nSection 506(f) of the Indian Health Care Improvement Act ( 25 U.S.C. 1656(f) ) is amended by striking , as defined in section 4(f) of this Act, .\n**(7)**\nSection 704(b) of the Indian Health Care Improvement Act ( 25 U.S.C. 1665c(b) ) is amended, in the subsection heading, by striking Contract Health Services and inserting Purchased/referred care .\n**(8)**\nSection 808 of the Indian Health Care Improvement Act ( 25 U.S.C. 1678 ) is amended, in the section heading, by striking contract health service and inserting purchased/referred care .\n**(9)**\nSection 808A of the Indian Health Care Improvement Act ( 25 U.S.C. 1678a ) is amended, in the section heading, by striking contract health service and inserting purchased/referred care .\n**(10)**\nSection 810 of the Indian Health Care Improvement Act ( 25 U.S.C. 1680 ) is amended by striking the section heading and designation and all that follows through The State and inserting the following:\n810. California as a purchased/referred care delivery area The State .\n**(11)**\nSection 815 of the Indian Health Care Improvement Act ( 25 U.S.C. 1680e ) is amended by striking the section heading and designation and all that follows through (a) The Secretary and inserting the following:\n815. Purchased/referred care for the Trenton service area (a) The Secretary .\n**(12)**\nSection 830(b) of the Indian Health Care Improvement Act ( 25 U.S.C. 1680t(b) ) is amended, in the subsection heading, by striking contract health services and inserting purchased/referred care .\n**(13)**\nSection 506A(a) of the Public Health Service Act (42 U.S.C. 290aa\u20135a(a)) is amended\u2014\n**(A)**\nin paragraph (2), by striking Tribal health program the second place it appears and inserting tribal health program ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking health program administered by the Service and inserting health program administered directly by the Service ; and\n**(ii)**\nby striking section 4(12)(A) of the Indian Health Care Improvement Act and inserting paragraph (11)(A) of section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ) .\n##### (c) Updating authorities\nThe Secretary of Health and Human Services is directed to ensure that the Indian Health Manual and all other relevant rules, guidance, manuals, and other materials are revised such that contract health service each place it appears (regardless of casing and typeface and including in the headings) is revised to read purchased/referred care (with appropriate casing and typeface).",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in Senate"
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
            "name": "Health care costs and insurance",
            "updateDate": "2026-02-11T15:13:38Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-02-11T15:13:52Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2026-02-11T15:13:11Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2026-02-11T15:13:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-09T13:04:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s699",
          "measure-number": "699",
          "measure-type": "s",
          "orig-publish-date": "2025-02-24",
          "originChamber": "SENATE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s699v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>"
        },
        "title": "Purchased and Referred Care Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s699.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s699"
    },
    "title": "Purchased and Referred Care Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Purchased and Referred Care Improvement Act of 2025</strong></p><p>This bill specifies that the Indian Health Service (IHS) must reimburse patients for their out-of-pocket costs for authorized purchased/referred care services within 30 days. (The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. However, when services are not available, IHS beneficiaries may be referred to private providers. This is called purchased/referred care.)</p><p>Specifically, the bill requires the Department of Health and Human Services (HHS) to establish and implement procedures to allow a patient who paid out of pocket for purchased/referred care services authorized by the IHS to be reimbursed by the IHS for that payment no later than 30 days after the patient submits required documentation.\u00a0</p><p>Additionally, the bill requires HHS to\u00a0update applicable provisions of and exhibits to the Indian Health Manual, contracts with providers, and other relevant documents and administrative authorities to incorporate the provisions of the bill.</p><p>The bill also replaces statutory references to <em>contract health service</em> with <em>purchased/referred care</em>.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s699"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s699is.xml"
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
      "title": "Purchased and Referred Care Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Purchased and Referred Care Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Indian Health Care Improvement Act to address liability for payment of charges or costs associated with the provision of purchased/referred care services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:23Z"
    }
  ]
}
```
