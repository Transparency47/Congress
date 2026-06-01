# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3639?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3639
- Title: VET PFAS Act
- Congress: 119
- Bill type: HR
- Bill number: 3639
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-04-16T08:06:39Z
- Update date including text: 2026-04-16T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3639",
    "number": "3639",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "VET PFAS Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:39Z",
    "updateDateIncludingText": "2026-04-16T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:42:55Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "RI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "IN"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CO"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MN"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NH"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MD"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "TN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "AZ"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3639ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3639\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Lawler (for himself, Mr. Riley of New York , Mr. Fitzpatrick , Ms. Tlaib , Mr. Magaziner , Ms. DelBene , Mr. Khanna , Ms. Chu , Mr. Carson , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to furnish hospital care and medical services to veterans and dependents who were stationed at military installations at which the veterans and dependents were exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances, to provide for a presumption of service connection for certain veterans who were stationed at military installations at which the veterans were exposed to such substances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Exposed to Toxic PFAS Act or the VET PFAS Act .\n#### 2. Hospital care and medical services for veterans and dependents exposed to perfluorooctanoic acid and other per- and polyfluoroalkyl substances\n##### (a) Hospital care and medical services for veterans\n**(1) In general**\nParagraph (1) of section 1710(e) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(J) (i) Beginning on the date that is 90 days after the date of the enactment of this subparagraph, subject to paragraph (2), a veteran who served on active duty in the Armed Forces at a covered military installation at which individuals were exposed to substances specified in clause (ii) is eligible for hospital care and medical services under subsection (a)(2)(F) for the diseases, illnesses, or conditions as specified in such clause, notwithstanding that there is insufficient medical evidence to conclude that such illness or condition is attributable to such service. (ii) The substances and diseases, illnesses, or conditions specified in this clause are the following: (I) With respect to exposure to perfluorooctanoic acid\u2014 (aa) diagnosed high cholesterol; (bb) ulcerative colitis; (cc) thyroid disease; (dd) testicular cancer; (ee) kidney cancer; and (ff) pregnancy-induced hypertension. (II) With respect to exposure to other per- and polyfluoroalkyl substances, any disease, illness, or condition that the Secretary of Veterans Affairs, in consultation with the Administrator of the Agency for Toxic Substances and Disease Registry of the Department of Health and Human Services, determines pursuant to the study conducted under section 316 of the National Defense Authorization Act for Fiscal Year 2018 ( Public Law 115\u201391 ) that a positive association exists between exposure to per- and polyfluoroalkyl substances and such disease, illness, or condition. (iii) For purposes of this subparagraph, any service by a member of the reserve components for a period specified by the Secretary at a covered military installation at which individuals were exposed to substances specified in clause (ii) shall be treated as active duty service, notwithstanding section 101(21) of this title. (iv) In this subparagraph, the term covered military installation means a military installation at which individuals were exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances, including exposure through a well that provides water for human consumption that is contaminated with such substances. .\n**(2) Limitation**\nParagraph (2)(B) of such section is amended by striking or (I) and inserting (I), or (J) .\n##### (b) Family members\n**(1) In general**\nSubchapter VIII of chapter 17 is amended by adding at the end the following new section:\n1787A. Health care of family members of veterans stationed at certain military installations (a) In general Beginning on the date that is 90 days after the date of the enactment of this section, subject to subsection (b), a family member of a veteran described in clause (i) of section 1710(e)(1)(J) of this title (or who would be so described but for the condition by which the individual was discharged or released from the Armed Forces) who resided at a military installation covered by such clause or who was in utero while the mother of such family member resided at such location shall be eligible for hospital care and medical services furnished by the Secretary for any disease, illness, or condition for which a veteran may receive hospital care and medical services under clause (ii) of such section, notwithstanding that there is insufficient medical evidence to conclude that such disease, illness, or condition is attributable to such residence. (b) Limitations (1) The Secretary may only furnish hospital care and medical services under subsection (a) to the extent and in the amount provided in advance in appropriations Acts for such purpose. (2) Hospital care and medical services may not be furnished under subsection (a) for a disease, illness, or condition of a family member that is found, in accordance with guidelines issued by the Under Secretary for Health, to have resulted from a cause other than the residence of the family member described in that subsection. (3) The Secretary may provide reimbursement for hospital care or medical services provided to a family member under this section only after the family member or the provider of such care or services has exhausted without success all claims and remedies reasonably available to the family member or provider against a third party (as defined in section 1725(f) of this title) for payment of such care or services, including with respect to health-plan contracts (as defined in such section). .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1787 the following new item:\n1787A. Health care of family members of veterans stationed at certain military installations. .\n##### (c) Annual reports\n**(1) In general**\nDuring the three-year period beginning in the year in which the study conducted under section 316 of the National Defense Authorization Act for Fiscal Year 2018 ( Public Law 115\u201391 ) is submitted to Congress, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives an annual report on the care and services provided under sections 1710(e)(1)(J) and 1787A of title 38, United States Code (as added by subsections (a) and (b)(1), respectively).\n**(2) Elements**\nEach report under paragraph (1) shall set forth the following:\n**(A)**\nThe number of veterans and family members provided hospital care and medical services under the provisions of law specified in paragraph (1) during the period covered by the report.\n**(B)**\nThe illnesses, conditions, and disabilities for which care and services have been provided such veterans and family members under such provisions of law during that period.\n**(C)**\nThe number of veterans and family members who applied for care and services under such provisions of law during that period but were denied, including information on the reasons for such denials.\n**(D)**\nThe number of veterans and family members who applied for care and services under such provisions of law and are awaiting a decision from the Secretary on eligibility for such care and services as of the date of such report.\n**(3) Veteran defined**\nIn this subsection, the term veteran includes a former member of the reserve components of the Armed Forces covered by such section 1710(e)(1)(J).\n#### 3. Presumption of service connection for certain veterans exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances\n##### (a) In general\nChapter 11 of title 38, United States Code, is amended by inserting after section 1116B the following new section:\n1116C. Presumption of service connection for certain veterans exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances (a) Presumption of service connection (1) For the purposes of section 1110 of this title, and subject to section 1113 of this title, each disease or illness specified in subsection (b) that becomes manifest in a veteran described in paragraph (2) shall be considered to have been incurred or aggravated in the line of duty in the active military, naval, or air service, notwithstanding that there is no record of evidence of such disease or illness during the period of such service. (2) A veteran described in this paragraph is a veteran who, during active military, naval, or air service, served at a military installation at which individuals were exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances, including exposure through a well that provides water for human consumption that is contaminated with such substances. (b) Diseases or illnesses A disease or illness specified in this subsection is any of the following: (1) With respect to exposure to perfluorooctanoic acid\u2014 (A) diagnosed high cholesterol; (B) ulcerative colitis; (C) thyroid disease; (D) testicular cancer; (E) kidney cancer; and (F) pregnancy-induced hypertension. (2) With respect to exposure to other per- and polyfluoroalkyl substances, any other disease, illness, or condition that the Secretary of Veterans Affairs, in consultation with the Administrator of the Agency for Toxic Substances and Disease Registry of the Department of Health and Human Services, determines pursuant to the study conducted under section 316 of the National Defense Authorization Act for Fiscal Year 2018 ( Public Law 115\u201391 ) that a positive association exists between exposure to per- and polyfluoroalkyl substances and such disease or illness. (c) Active military, naval, or air service For purposes of this section, any service by a member of the reserve components for a period specified by the Secretary at a military installation described in subsection (a)(2) shall be treated as active military, naval, or air service, notwithstanding section 101(24) of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1116B the following new item:\n1116C. Presumption of service connection for certain veterans exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances. .",
      "versionDate": "2025-05-29",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-10T22:48:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
    "originChamber": "House",
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
          "measure-id": "id119hr3639",
          "measure-number": "3639",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3639v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Exposed to Toxic PFAS Act or the VET PFAS Act</strong></p> <p>This bill provides eligibility for Department of Veterans Affairs (VA) hospital care and medical services to veterans and their family members (including those in utero) who have specified conditions and resided at a military installation where individuals were exposed to perfluoroalkyl and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p> <p>Hospital care and medical services may not be furnished for a condition that is found to have resulted from a cause other than the exposure to PFAS at a military installation.</p> <p>The VA may provide reimbursement for hospital care or medical services provided to a family member only after the family member or provider has exhausted all claims and remedies otherwise available for payment of such care.</p> <p>For disability compensation purposes, the bill establishes a presumption of service-connection for specified conditions in veterans who served at a military installation at which individuals were exposed to PFAS. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.<br/> </p>"
        },
        "title": "VET PFAS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3639.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Exposed to Toxic PFAS Act or the VET PFAS Act</strong></p> <p>This bill provides eligibility for Department of Veterans Affairs (VA) hospital care and medical services to veterans and their family members (including those in utero) who have specified conditions and resided at a military installation where individuals were exposed to perfluoroalkyl and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p> <p>Hospital care and medical services may not be furnished for a condition that is found to have resulted from a cause other than the exposure to PFAS at a military installation.</p> <p>The VA may provide reimbursement for hospital care or medical services provided to a family member only after the family member or provider has exhausted all claims and remedies otherwise available for payment of such care.</p> <p>For disability compensation purposes, the bill establishes a presumption of service-connection for specified conditions in veterans who served at a military installation at which individuals were exposed to PFAS. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.<br/> </p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3639"
    },
    "title": "VET PFAS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Exposed to Toxic PFAS Act or the VET PFAS Act</strong></p> <p>This bill provides eligibility for Department of Veterans Affairs (VA) hospital care and medical services to veterans and their family members (including those in utero) who have specified conditions and resided at a military installation where individuals were exposed to perfluoroalkyl and polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p> <p>Hospital care and medical services may not be furnished for a condition that is found to have resulted from a cause other than the exposure to PFAS at a military installation.</p> <p>The VA may provide reimbursement for hospital care or medical services provided to a family member only after the family member or provider has exhausted all claims and remedies otherwise available for payment of such care.</p> <p>For disability compensation purposes, the bill establishes a presumption of service-connection for specified conditions in veterans who served at a military installation at which individuals were exposed to PFAS. Under a presumption of service-connection, specific conditions diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.<br/> </p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3639"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3639ih.xml"
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
      "title": "VET PFAS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VET PFAS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Exposed to Toxic PFAS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to furnish hospital care and medical services to veterans and dependents who were stationed at military installations at which the veterans and dependents were exposed to perfluorooctanoic acid or other per- and polyfluoroalkyl substances, to provide for a presumption of service connection for certain veterans who were stationed at military installations at which the veterans were exposed to such substances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T05:18:31Z"
    }
  ]
}
```
