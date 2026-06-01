# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5316
- Title: Drug Shortage Compounding Patient Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5316
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-10-25T08:05:41Z
- Update date including text: 2025-10-25T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5316",
    "number": "5316",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Drug Shortage Compounding Patient Access Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:41Z",
    "updateDateIncludingText": "2025-10-25T08:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:05:15Z",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "GA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "UT"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5316ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5316\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mrs. Harshbarger (for herself and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to ensure patients have access to certain shortage and urgent-use compounded medications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Shortage Compounding Patient Access Act of 2025 .\n#### 2. Pharmacy compounding\n##### (a) Compounding for urgent administration to patients\nSection 503A(a) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking or at the end;\n**(2)**\nin paragraph (2)(B)(ii)(II), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(3) notwithstanding the requirement in the matter preceding paragraph (1) that the drug product is compounded for an identified individual patient based on a valid prescription order or notation described in such matter, is by a licensed pharmacist or licensed physician and the compounded drug product is compounded for distribution in limited quantities to a licensed prescriber for urgent administration to a patient in a hospital or other clinical setting, provided that all of the following are met: (A) The drug product appeared on the drug shortage list in effect under section 506E at any time during the 60-day period ending on the date of the compounding, distribution, or dispensing of the drug product. (B) The licensed prescriber certifies by notation on the order to the compounding pharmacist or physician that the licensed prescriber has made reasonable attempts to obtain, and has not been able to obtain, to address the urgent medical need a drug product that is compounded by an outsourcing facility in accordance with section 503B with the same active ingredient and the same route of administration. (C) The compounded drug product is labeled with a beyond-use-date in accordance with applicable United States Pharmacopeia standards. (D) The licensed pharmacist or licensed physician marks the packaging of the compounded drug product with text\u2014 (i) indicating that the drug product is provided to the hospital or other clinical setting only for urgent administration to a patient; and (ii) requesting that the hospital or other clinical setting provide to the compounding pharmacist or physician the records that identify the patient or patients to whom the drug products were administered within\u2014 (I) 7 days of each such patient receiving such medication; or (II) 7 days of each such patient being discharged. (E) Upon receipt of records requested pursuant to subparagraph (D)(ii), the licensed pharmacist or licensed physician ensures that the patient information in such records is linked with the respective order. (F) The licensed pharmacist or licensed physician reports adverse events associated with the compounded drug product as soon as possible but not later than 15 days after becoming aware of such events to the MedWatch Adverse Event Reporting program of the Food and Drug Administration (or any successor program). .\n##### (b) Definition\nParagraph (2) of section 503A(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a(b)(2) ) is amended to read as follows:\n(2) Definition For purposes of paragraph (1)(D), the term essentially a copy of a commercially available drug product does not include\u2014 (A) a drug product in which there is a change, made for an identified individual patient, which produces for that patient a significant difference, as determined by the prescribing practitioner, between the compounded drug and the comparable commercially available drug product; or (B) a drug product that meets each of the following conditions: (i) At any time during the 60-day period ending on the date of the compounding, distribution, or dispensing, the drug product appeared on the drug shortage list in effect under section 506E. (ii) If the drug product is not compounded for an identified individual patient based on a valid prescription order or notation, notwithstanding such requirement in the matter preceding paragraph (1) of subsection (a), the drug product\u2014 (I) is labeled in accordance subparagraphs (C) and (D) of subsection (a)(3); and (II) is documented by the compounding pharmacist or physician in accordance with subparagraphs (E) and (F) of subsection (a)(3). .\n#### 3. Mitigating drug shortages through improved reporting\nSection 506C of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c ) is amended\u2014\n**(1)**\nin the section heading, by inserting OR SURGE IN DEMAND FOR after PRODUCTION OF ;\n**(2)**\nin subsection (a), in the matter following paragraph (2)\u2014\n**(A)**\nby striking or an interruption of the manufacture of the drug and inserting , an interruption of the manufacture of the drug, or a surge in demand for the drug ;\n**(B)**\nby striking such discontinuance or interruption and inserting such discontinuance, interruption, or surge in demand ;\n**(C)**\nby striking the discontinuation or interruption and inserting the discontinuation, interruption, or surge in demand ;\n**(D)**\nby striking such discontinuation or interruption, the source and inserting such discontinuation, interruption, or surge in demand, the source ; and\n**(E)**\nby striking such discontinuation or interruption; the expected duration of the interruption; and inserting such discontinuation, interruption, or surge in demand; the expected duration of the interruption or surge in demand ;\n**(3)**\nin subsection (b), by striking paragraphs (1) and (2) and inserting the following:\n(1) in the case of a notice of a discontinuance or interruption in the manufacture of a drug\u2014 (A) at least 6 months prior to the date of the discontinuance or interruption; or (B) if compliance with subparagraph (A) is not possible, as soon as practicable; or (2) in the case of a notice of a surge in demand for a drug, as soon as practicable. ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nby striking discontinuance or interruption and inserting discontinuance, interruption, or surge in demand ; and\n**(B)**\nby inserting and outsourcing facilities (as defined in section 503B(d)) after patient organizations ; and\n**(5)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (1), by striking and that is subject to section 503(b)(1) and inserting or the active pharmaceutical ingredient of such a drug ;\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) the term drug shortage or shortage , with respect to a drug, means a period of time with the demand or projected demand for the drug within the United States exceeds the supply of the drug, taking into consideration\u2014 (A) how the drug is prepared or dispensed, including the route of administration and dosage form; and (B) information reported by manufacturers, health care professionals, and patients; .\n**(C)**\nin paragraph (3)(B), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(4) the term surge means an increase in demand or projected demand for a drug that the manufacturer likely will be unable to meet without meaningful shortfall or delay. .\n#### 4. Outsourcing facility compounding\nSection 503B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353b ) is amended\u2014\n**(1)**\nin subsection (a)(2)(A)(ii)\u2014\n**(A)**\nby striking appears and inserting appeared ; and\n**(B)**\nby striking at the time of and inserting at any time during the 180-day period ending on the date of ;\n**(2)**\nin subsection (a)(10)(A)(iii)\u2014\n**(A)**\nin subclause (VIII), by striking the semicolon at the end and inserting ; and ;\n**(B)**\nby striking subclause (IX); and\n**(C)**\nby redesignating subclause (X) as subclause (IX);\n**(3)**\nby redesignating the 2 subsections (d) (relating to definitions and relating to obligation to pay fees) as subsections (e) and (f), respectively; and\n**(4)**\nby inserting after subsection (c) the following:\n(d) List of identified bulk drug substances The Secretary shall make publicly available annual updates on the evaluation of bulk drug substances for purposes of the list maintained under subsection (a)(2)(A)(i). ;\n#### 5. Clarifying provisions; labeling requirement\nSection 503A of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353a ) is amended\u2014\n**(1)**\nby striking subsection (b)(3)(B) and the matter following such subsection and inserting the following:\n(B) such drug product is labeled as follows: This medication has been compounded for dispensing to an individual patient and has not been approved by the Food and Drug Administration . ; and\n**(2)**\nin subsection (b)(1)(A)(i)(I) by striking National Formulary monograph and inserting National Formulary drug or dietary supplement monograph .",
      "versionDate": "2025-09-11",
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
        "name": "Health",
        "updateDate": "2025-09-24T15:04:00Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5316ih.xml"
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
      "title": "Drug Shortage Compounding Patient Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drug Shortage Compounding Patient Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to ensure patients have access to certain shortage and urgent-use compounded medications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:33:33Z"
    }
  ]
}
```
