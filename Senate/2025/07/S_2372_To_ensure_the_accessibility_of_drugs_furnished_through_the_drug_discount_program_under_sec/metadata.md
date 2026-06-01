# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2372
- Title: 340B PATIENTS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2372
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2025-12-05T22:47:52Z
- Update date including text: 2025-12-05T22:47:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2372",
    "number": "2372",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "340B PATIENTS Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:47:52Z",
    "updateDateIncludingText": "2025-12-05T22:47:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T17:03:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "OR"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2372is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2372\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Welch (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure the accessibility of drugs furnished through the drug discount program under section 340B of the Public Health Service Act.\n#### 1. Short title\nThis Act may be cited as the 340B Pharmaceutical Access To Invest in Essential, Needed Treatments & Support Act of 2025 or the 340B PATIENTS Act of 2025 .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nSection 340B of the Public Health Service Act ( 42 U.S.C. 256b ) enables covered entities to stretch scarce resources as far as possible, reaching more patients and providing more comprehensive services than would be possible without such program.\n**(2)**\nSuch section 340B requires drug manufacturers to offer discounted prices on covered outpatient drugs to covered entities participating in the program, and, as a condition of participating in the Medicaid program and part B of the Medicare program, drug manufacturers are required to offer drug discount pricing to covered entities when requested.\n**(3)**\nSavings on the purchase of drugs under the drug discount program under section 340B of the Public Health Service Act enables hospitals, clinics, and health centers to provide comprehensive services to the communities they serve, and covered entities are in the best position to assess the use of their savings for community needs.\n**(4)**\nSince the early years of such program, covered entities have contracted with pharmacies to dispense covered outpatient drugs purchased by a covered entity at drug discount program pricing to patients of the covered entity, consistent with how Congress intended for covered entities to use the program.\n**(5)**\nCovered entities use savings generated through contract pharmacy relationships to stretch scarce resources and support patient care, consistent with the purpose of the program.\n**(6)**\nSection 340B of the Public Health Service Act requires drug manufacturers to offer discount pricing for drugs purchased by covered entities regardless of the manner or location in which a drug is dispensed, including drugs dispensed through contract pharmacies.\n**(7)**\nSuch section 340B does not allow drug manufacturers to place conditions on the ability of a covered entity to purchase or use a covered outpatient drug at discounted pricing regardless of the manner or location in which a drug is dispensed, including by restricting a covered entity\u2019s ability to dispense drugs purchased at such discount to patients through a contractual relationship with a contracted pharmacy or refusing to ship covered outpatient drugs to a pharmacy or location identified by a covered entity.\n**(8)**\nThe inflationary penalty provisions under section 340B of the Public Health Service Act, which have saved $7,000,000,000 in spending under part D of the Medicare program between 2013 and 2017, have a proven record of reducing drug price increases, and use of the drug discount program in contract pharmacies contributes to these savings.\n**(9)**\nSpecialty drugs, which are often used to treat chronic, serious, or life-threatening conditions such as cancer, rheumatoid arthritis, growth hormone deficiency, and multiple sclerosis, play a critical role in the care provided by covered entities. These drugs often require specialized handling, are not usually available to walk-in customers, and are typically available only through specialty or mail order pharmacies that are located hundreds of miles from a covered entity. The use of contract pharmacy arrangements under section 340B of the Public Health Service Act are often the only means by which covered entities can access these vital drugs.\n##### (b) Purposes\nThe purposes of this Act are the following:\n**(1)**\nTo clarify that section 340B of the Public Health Service Act ( 42 U.S.C. 256b )\u2014\n**(A)**\nrequires drug manufacturers to offer drug discount pricing pursuant to an agreement under subsection (a) of such section with respect to drugs purchased by a covered entity regardless of the manner or location in which the drug is dispensed; and\n**(B)**\nprohibits drug manufacturers from placing conditions on the ability of covered entities to purchase covered outpatient drugs pursuant to an agreement under subsection (a) of such section, regardless of the manner or location in which they are dispensed.\n**(2)**\nTo clarify that\u2014\n**(A)**\ncovered entities may contract with pharmacies to dispense drugs purchased pursuant to an agreement under section 340B(a) of the Public Health Service Act ( 42 U.S.C. 256b(a) ) on a covered entity\u2019s behalf, to assist covered entities in stretching resources to provide care to more patients and provide more comprehensive services; and\n**(B)**\nthe requirements and prohibitions that apply to manufacturers under section 340B of such Act apply in the case of a covered entity that elects to contract with a pharmacy to dispense covered outpatient drugs.\n#### 3. Ensuring the accessibility of drugs furnished under the drug discount program\n##### (a) In general\nSection 340B(a) of the Public Health Service Act ( 42 U.S.C. 256b(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking that the manufacturer furnish and inserting the following:\nthat\u2014 (A) the manufacturer furnish ;\n**(B)**\nby striking ceiling price ), and and inserting ceiling price ); ;\n**(C)**\nby striking shall require that the manufacturer offer and inserting the following:\n(B) the manufacturer offer ; and\n**(D)**\nby striking the period at the end and inserting the following:\n, regardless of the manner or location in which the drug is dispensed; and (C) the manufacturer not place any conditions on the ability of a covered entity to purchase and use a covered outpatient drug at or below the applicable ceiling price, regardless of the manner or location in which the drug is dispensed, if such conditions\u2014 (i) would place limits on the delivery of drugs, place limits on the mechanisms through which drugs may be purchased, place limits on where such drugs may be delivered, administered, or dispensed, require a covered entity\u2019s assurance of compliance with requirements under this section, or require the submission of claims data or other information; (ii) would not reflect customary business practices; (iii) would discourage covered entities from purchasing the manufacturer\u2019s drugs through the drug discount program under this section or otherwise undermine the objective of this section, either by singling out covered entities from other customers for such conditions or by imposing conditions that disproportionately impact covered entities; or (iv) have not been approved in advance by the Secretary. ; and\n**(2)**\nby adding at the end the following new paragraph:\n(11) Contract Pharmacies The requirements and prohibitions under paragraph (1) shall apply in the case of a covered entity that elects to contract with one or more pharmacies to dispense, to patients of the covered entity, covered outpatient drugs purchased by the covered entity at or below the applicable ceiling price described in paragraph (1). .\n##### (b) Manufacturer compliance\nSection 340B(d) of the Public Health Service Act ( 42 U.S.C. 256b ) is amended\u2014\n**(1)**\nin paragraph (1)(B)\u2014\n**(A)**\nin clause (vi), in the matter preceding subclause (I), by inserting , in the case of a manufacturer overcharging a covered entity for covered outpatient drugs after penalties ; and\n**(B)**\nby adding at the end the following:\n(vii) The imposition of sanctions in the form of civil monetary penalties in the case of a violation of subsection (a)(1)(C) or (a)(11), other than an overcharge, which\u2014 (I) shall be assessed according to standards established in regulations to be promulgated by the Secretary not later than 180 days after the date of enactment; (II) shall apply to any manufacturer with an agreement under this section that intentionally violates a requirement under subsection (a)(1)(C) or (a)(11), other than an overcharge; (III) shall not exceed $2,000,000 for each day of such violation; (IV) shall be in an amount determined by the Secretary, taking into account factors such as the nature and extent of the violation and harm resulting from such violation, including, where applicable, the number of drugs affected and the number of covered entities affected; and (V) shall continue to be imposed each day until such manufacturer is no longer in violation of a requirement under subsection (a)(1)(C) or (a)(11), other than an overcharge. ; and\n**(2)**\nin paragraph (3), by adding at the end the following:\n(D) Claims of violations Not later than 180 days after the date of the enactment of this subparagraph, the Secretary shall promulgate regulations to permit covered entities to assert claims of violations of subsections (a)(1) and (a)(11) under the process established under subparagraph (A). .",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4581",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "340B PATIENTS Act of 2025",
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
        "updateDate": "2025-09-05T16:21:04Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2372is.xml"
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
      "title": "340B PATIENTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "340B PATIENTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "340B Pharmaceutical Access To Invest in Essential, Needed Treatments & Support Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure accessibility of drugs furnished through the drug discount program under section 340B of the Public Health Service Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:15Z"
    }
  ]
}
```
