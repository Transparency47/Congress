# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/760?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/760
- Title: Kids’ Access to Primary Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 760
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-12-05T21:35:04Z
- Update date including text: 2025-12-05T21:35:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/760",
    "number": "760",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Kids\u2019 Access to Primary Care Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:35:04Z",
    "updateDateIncludingText": "2025-12-05T21:35:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
        "item": {
          "date": "2025-02-26T22:31:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s760is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 760\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mrs. Murray (for herself, Mr. Warnock , Mr. Booker , Mr. Blumenthal , Mr. Luj\u00e1n , Mr. Merkley , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to renew the application of the Medicare payment rate floor to primary care services furnished under the Medicaid program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kids\u2019 Access to Primary Care Act of 2025 .\n#### 2. Renewal of application of Medicare payment rate floor to primary care services furnished under Medicaid and inclusion of additional providers\n##### (a) Renewal of payment floor; additional providers\n**(1) In general**\nSection 1902(a)(13) of the Social Security Act ( 42 U.S.C. 1396a(a)(13) ) is amended by striking subparagraph (C) and inserting the following:\n(C) payment for primary care services (as defined in subsection (jj)) at a rate that is not less than 100 percent of the payment rate that applies to such services and physician under part B of title XVIII (or, if greater, the payment rate that would be applicable under such part if the conversion factor under section 1848(d) for the year involved were the conversion factor under such section for 2009), and that is not less than the rate that would otherwise apply to such services under this title if the rate were determined without regard to this subparagraph, and that are\u2014 (i) furnished in 2013 and 2014, by a physician with a primary specialty designation of family medicine, general internal medicine, or pediatric medicine; or (ii) furnished during the period beginning on the first day of the first month beginning after the date of the enactment of the Kids\u2019 Access to Primary Care Act of 2025 \u2014 (I) by a physician with a primary specialty designation of family medicine, general internal medicine, pediatric medicine, or obstetrics and gynecology, but only if the physician self-attests that the physician is board-certified in family medicine, general internal medicine, pediatric medicine, or obstetrics and gynecology, respectively; (II) by a physician with a primary specialty designation of a family medicine subspecialty, an internal medicine subspecialty, a pediatric subspecialty, or a subspecialty of obstetrics and gynecology, without regard to the board that offers the designation for such a subspecialty, but only if the physician self-attests that the physician is board-certified in such a subspecialty; (III) by an advanced practice clinician, as defined by the Secretary, that works under the supervision of\u2014 (aa) a physician described in subclause (I) or (II); or (bb) a nurse practitioner or a physician assistant (as such terms are defined in section 1861(aa)(5)(A)) who is working in accordance with State law, or a certified nurse-midwife (as defined in section 1861(gg)(2)) who is working in accordance with State law; (IV) by a rural health clinic, Federally-qualified health center, or other health clinic that receives reimbursement on a fee schedule applicable to a physician described in subclause (I) or (II), an advanced practice clinician described in subclause (III), or a nurse practitioner, physician assistant, or certified nurse-midwife described in subclause (III)(bb), for services furnished by\u2014 (aa) such a physician, nurse practitioner, physician assistant, or certified nurse-midwife, respectively; or (bb) an advanced practice clinician supervised by such a physician, nurse practitioner, physician assistant, or certified nurse-midwife; or (V) by a nurse practitioner or a physician assistant (as such terms are defined in section 1861(aa)(5)(A)) who is working in accordance with State law, or a certified nurse-midwife described in subclause (III)(bb) who is working in accordance with State law, in accordance with procedures that ensure that the portion of the payment for such services that the nurse practitioner, physician assistant, or certified nurse-midwife is paid is not less than the amount that the nurse practitioner, physician assistant, or certified nurse-midwife would be paid if the services were provided under part B of title XVIII; .\n**(2) Conforming amendments**\nSection 1905(dd) of the Social Security Act ( 42 U.S.C. 1396d(dd) ) is amended\u2014\n**(A)**\nby striking Notwithstanding and inserting the following:\n(1) In general Notwithstanding ;\n**(B)**\nby inserting or furnished during the additional period specified in paragraph (2), after 2015, ; and\n**(C)**\nby adding at the end the following:\n(2) Additional period For purposes of paragraph (1), the additional period specified in this paragraph is the period beginning on the first day of the first month beginning after the date of the enactment of the Kids\u2019 Access to Primary Care Act of 2025 . .\n##### (b) Improved targeting of primary care\n**(1) In general**\nSection 1902(jj) of the Social Security Act ( 42 U.S.C. 1396a(jj) ) is amended\u2014\n**(A)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and moving the margin of each such subparagraph, as so redesignated, 2 ems to the right;\n**(B)**\nby striking For purposes of and inserting the following:\n(1) In general For purposes of ; and\n**(C)**\nby adding at the end the following:\n(2) Exclusions Such term does not include any services described in subparagraph (A) or (B) of paragraph (1) if such services are provided in an emergency department of a hospital. .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply with respect to primary care services provided on or after the first day of the period described in subparagraph (C)(ii) of section 1902(a)(13) of the Social Security Act ( 42 U.S.C. 1396a(a)(13) ), as amended by section 2.\n##### (c) Ensuring payment by managed care entities\n**(1) In general**\nSection 1903(m)(2)(A) of the Social Security Act ( 42 U.S.C. 1396b(m)(2)(A) ) is amended\u2014\n**(A)**\nin clause (xii), by striking and after the semicolon;\n**(B)**\nin clause (xiii)\u2014\n**(i)**\nby moving the margin of such clause 2 ems to the left; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after clause (xiii) the following:\n(xiv) such contract provides that (I) payments to health care providers specified in section 1902(a)(13)(C) for furnishing primary care services defined in section 1902(jj) during a year or period specified in section 1902(a)(13)(C) are at least equal to the amounts set forth and required by the Secretary by regulation, (II) the entity shall, upon request, provide documentation to the State that is sufficient to enable the State and the Secretary to ensure compliance with subclause (I), and (III) the Secretary shall approve payments described in subclause (I) that are furnished through an agreed-upon capitation, partial capitation, or other value-based payment arrangement if the agreed-upon capitation, partial capitation, or other value-based payment arrangement is based on a reasonable methodology and the entity provides documentation to the State that is sufficient to enable the State and the Secretary to ensure compliance with subclause (I). .\n**(2) Conforming amendment**\nSection 1932(f) of the Social Security Act ( 42 U.S.C. 1396u\u20132(f) ) is amended by inserting and clause (xiv) of section 1903(m)(2)(A) before the period.\n**(3) Effective date**\nThe amendments made by this subsection shall apply with respect to contracts entered into on or after the date of the enactment of this Act.\n#### 3. Study\n##### (a) In general\nNot later than the date that is one year and one month after the date of the enactment of this Act, the Secretary of Health and Human Services shall conduct a study\u2014\n**(1)**\ncomparing the number of children enrolled in a State plan under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) (or a waiver of such plan) during the 12-month period preceding the first day of the period described in subparagraph (C)(ii) of section 1902(a)(13) of such Act ( 42 U.S.C. 1396a(a)(13) ), as amended by section 2, to the number of children so enrolled during the 12-month period beginning on such first day;\n**(2)**\ncomparing the number of health care providers receiving payments for primary care services under the Medicaid program under such title during the 12-month period preceding the first day of the period described in subparagraph (C)(ii) of section 1902(a)(13) of such Act ( 42 U.S.C. 1396a(a)(13) ), as amended by section 2, to the number of health care providers receiving such payments during the 12-month period beginning on such first day; and\n**(3)**\ncomparing health care provider payment rates for primary care services under the Medicaid program under such title during the 12-month period beginning on the first day of the period described in subparagraph (C)(ii) of section 1902(a)(13) of such Act ( 42 U.S.C. 1396a(a)(13) ), as amended by section 2, across States, using the indexes described in subsection (b).\n##### (b) Indexes described\nThe indexes described in this subsection are each of the following:\n**(1)**\nA Medicaid fee index, comparing each State\u2019s average fee for primary care services under the Medicaid program under such title to the national average for such services.\n**(2)**\nA Medicaid-to-Medicare fee index, comparing each State\u2019s average fee for primary care services under the Medicaid program under such title to the fee for such services under the Medicare program under title XVIII of such Act ( 42 U.S.C. 1395 et seq. ).\n**(3)**\nA Medicaid fee change index, comparing fees for primary care services under the Medicaid program under such title during the 12-month period preceding the first day of the period described in subparagraph (C)(ii) of section 1902(a)(13) of such Act ( 42 U.S.C. 1396a(a)(13) ), as amended by section 2, to the fees for such services during the 12-month period beginning on such first day.\n##### (c) Authorization of appropriations\nFor purposes of this section, there is authorized to be appropriated $200,000 for fiscal year 2026, to be available until expended.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-02-18",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1433",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kids\u2019 Access to Primary Care Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-07-09T14:26:01Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-07-09T14:26:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T16:26:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s760",
          "measure-number": "760",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s760v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Kids' Access to Primary Care Act of 2025</strong><strong></strong></p><p>This bill modifies payments for Medicaid primary care services. Specifically, the bill applies a Medicare payment rate floor to Medicaid primary care services that are provided after the date of enactment of the bill and extends the payment rate to additional types of practitioners (e.g., obstetricians).</p><p>The Centers for Medicare & Medicaid Services must conduct a study on the number of children enrolled in Medicaid, the number of providers receiving payment for primary care services, and associated payment rates before and after the bill's implementation.</p>"
        },
        "title": "Kids\u2019 Access to Primary Care Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s760.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Kids' Access to Primary Care Act of 2025</strong><strong></strong></p><p>This bill modifies payments for Medicaid primary care services. Specifically, the bill applies a Medicare payment rate floor to Medicaid primary care services that are provided after the date of enactment of the bill and extends the payment rate to additional types of practitioners (e.g., obstetricians).</p><p>The Centers for Medicare & Medicaid Services must conduct a study on the number of children enrolled in Medicaid, the number of providers receiving payment for primary care services, and associated payment rates before and after the bill's implementation.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s760"
    },
    "title": "Kids\u2019 Access to Primary Care Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Kids' Access to Primary Care Act of 2025</strong><strong></strong></p><p>This bill modifies payments for Medicaid primary care services. Specifically, the bill applies a Medicare payment rate floor to Medicaid primary care services that are provided after the date of enactment of the bill and extends the payment rate to additional types of practitioners (e.g., obstetricians).</p><p>The Centers for Medicare & Medicaid Services must conduct a study on the number of children enrolled in Medicaid, the number of providers receiving payment for primary care services, and associated payment rates before and after the bill's implementation.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s760"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s760is.xml"
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
      "title": "Kids\u2019 Access to Primary Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kids\u2019 Access to Primary Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to renew the application of the Medicare payment rate floor to primary care services furnished under the Medicaid program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:30Z"
    }
  ]
}
```
