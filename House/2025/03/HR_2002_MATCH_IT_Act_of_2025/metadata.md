# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2002
- Title: MATCH IT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2002
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-21T08:07:53Z
- Update date including text: 2026-05-21T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2002",
    "number": "2002",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "MATCH IT Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:53Z",
    "updateDateIncludingText": "2026-05-21T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-10T16:04:50Z",
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
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "AL"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2002ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2002\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Kelly of Pennsylvania (for himself, Mr. Foster , and Mr. Moulton ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XXX of the Public Health Service Act to establish standards and protocols to improve patient matching.\n#### 1. Short title\nThis Act may be cited as the Patient Matching And Transparency in Certified Health IT Act of 2025 or the MATCH IT Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEnsuring accurate patient identification and matching is key to achieving the interoperability within the health care system called for by Congress in the 21st Century Cures Act and the Health Information Technology for Economic and Clinical Health (HITECH) Act.\n**(2)**\nThere is currently no national strategy to ensure patients are accurately matched with their medical records.\n**(3)**\nThere is no standard definition across the health care system of patient match rate to ensure the ability to accurately measure patient matches and patient misidentification.\n**(4)**\nThe patient match rates that are available can vary widely, with an estimate from CHIME noting that matching within facilities can be as low as 80 percent\u2014meaning that one out of every five patients may not be matched to all his or her records.\n**(5)**\nPatient misidentification within the United States health care system is a threat to patient safety, patient privacy, and a driver of unnecessary costs to patients and providers.\n**(6)**\nThe inability of clinicians to ensure patients are accurately matched with their medical record has caused medical errors, and even lives lost. Patient misidentification has been named a recurrent patient safety challenge in multiple years by ECRI.\n**(7)**\nPatients must undergo unnecessary repeated medical tests because of the inability to ensure accurate matches to their medical record.\n**(8)**\nThe expense of repeated medical care due to duplicate records costs an average of $1,950 per patient inpatient stay, and more than $1,700 per emergency department visit. Thirty-five percent of all denied claims result from inaccurate patient identification, costing the average hospital $2.5 million and the United States health care system more than $6.7 billion annually.\n**(9)**\nOverlaid records, caused by merging multiple patients\u2019 data into one medical record, may result in unauthorized disclosures under the Health Insurance Portability and Accountability Act (HIPAA), as well as the risk of a patient receiving treatment for another patient\u2019s condition.\n**(10)**\nThis Act would decrease the prevalence of patient misidentification by further promoting interoperability, thereby protecting patients and addressing high costs driven by this issue.\n#### 3. Standards and protocols to improve patient matching\n##### (a) In general\nSubtitle C of title XXX of the Public Health Service Act ( 42 U.S.C. 300jj\u201351 et seq. ) is amended by adding at the end the following new section:\n3023. Standards and protocols to improve patient matching (a) Establishing a uniform definition for patient match rate (1) In general Not later than 180 days after the date of enactment of this section, the Secretary shall, in consultation with health care providers, vendors of electronic health records and health information technology, patient groups, and other relevant stakeholders, develop a definition and standards for accurate and precise patient matching to track patient match rates and document improvements of patient matching over time. The Secretary shall ensure that such definition and standards for patient match rate account for\u2014 (A) duplicate records; (B) overlaid records; (C) instances of multiple matches found; and (D) mismatch rates within the same healthcare organizations and provider systems. (2) Review and update In consultation with health care providers, vendors of electronic health records and health information technology, patient groups, and other relevant stakeholders, the Secretary shall review and update the definition and standards developed under paragraph (1), as appropriate, not less frequently than once every 3 years to ensure that such definition and standards are consistent with updates and improvements in technologies and processes. (b) Development of a standard data set To improve patient matching (1) In general Not later than 180 days after the date of enactment of this section, subject to paragraph (2), the National Coordinator shall review the current data set in the United States Core Data for Interoperability and identify, define, and adopt the minimum data set needed to support the adoption of patient matching by entities, including health care providers, developers of health care information technology or certified health IT, or health information networks of exchange, at a rate of 99.9 percent. The National Coordinator shall include such minimum data set in the United States Core Data for Interoperability. (2) Development of data standards in United States core data for interoperability For purposes of improving interoperable health exchange, not later than 1 year after defining the minimum data set described in paragraph (1), the National Coordinator shall create, update, or adopt data standards for the data elements identified in the minimum data set and incorporate such standards into the United States Core Data for Interoperability. (3) Consultation required In identifying and defining the minimum data set described in paragraph (1) and creating, updating, or adopting data standards described in paragraph (2), the National Coordinator shall consult with\u2014 (A) health care providers; (B) vendors of electronic health records; (C) vendors of health information technology; (D) patient groups; (E) Federal agencies, including the National Institute of Standards and Technology, the Centers for Disease Control and Prevention, the Department of Defense, the National Institutes of Health, the Department of Veterans Affairs, the Social Security Administration, the Indian Health Service, and the Office for Civil Rights; (F) public health authorities within State, local, territorial, and Tribal; and (G) any other stakeholders the Secretary determines appropriate. (4) Rule of construction Nothing in this subsection shall be construed to require an entity to meet a minimum patient match rate of 99.9 percent. .\n##### (b) Incorporating the minimum data set for patient matching into certification requirements\nSection 3004(b) of subtitle B of title XXX of the Public Health Service Act ( 42 U.S.C. 300jj\u201314(b) ) is amended by adding at the end the following new subparagraph:\n(4) Special rule (A) Incorporation of minimum data set into health it certification requirements Notwithstanding paragraph (3), the Secretary shall incorporate and adopt the minimum data set for patient matching established under section 3023 into the certification criteria adopted under this section not later than 180 days after such data set is finalized. (B) Incorporation of minimum data set into Medicare interoperability program requirements Not later than 24 months after the incorporation of the minimum data set for patient matching into the certification criteria as required in subparagraph (A), the Secretary shall incorporate and adopt such minimum data set for patient matching established under section 3023 into program requirements to promote the interoperability of certified EHR technology for entities participating in the Medicare program under title XVIII of the Social Security Act. .\n##### (c) Additional incentives To promote interoperability\n**(1) In general**\nNot later than 24 months after the incorporation and adoption of the minimum data set for patient matching into the program requirements to promote the interoperability of certified EHR technology for entities participating under the Medicare program under title XVIII of the Social Security Act as required in subparagraph (B) of section 3004(b)(4) of title XXX of the Public Health Service Act ( 42 U.S.C. 300jj\u201314(b) ), the Administrator of the Centers for Medicare and Medicaid Services shall, through rulemaking, establish a voluntary bonus measure within the Medicare Promoting Interoperability Program for eligible providers who meet an accurate patient match rate (as defined under section 3023 of subtitle C of title XXX of the Public Health Service Act) of at least 90 percent or the rate determined under paragraph (4) to voluntary attest to and receive a payment adjustment for meeting such measure.\n**(2) Special rule**\nIn establishing the voluntary bonus measure described in paragraph (1), the Administrator shall\u2014\n**(A)**\nensure that the total score for incentive payments or status as an eligible provider will not be negatively impacted if the eligible provider does not attest to an accurate patient match rate; and\n**(B)**\nensure that the voluntary attestations regarding patient matching rates shall not be publicly disclosed.\n**(3) Voluntary reporting program**\nThe National Coordinator, along with the Centers for Medicare and Medicaid Services and other Federal agencies determined appropriate by the Secretary, shall develop a voluntary reporting program for eligible providers to anonymously submit patient matching accuracy data to the Department of Health and Human Services.\n**(4) Annual review of patient match rate**\n**(A) In general**\nUtilizing the patient matching accuracy data described in paragraph (2) and any additional data sources available, the Administrator of the Centers of Medicare and Medicaid Services shall review and evaluate the patient match attestation rates annually to determine if such rate should be adjusted.\n**(B) Adjustment**\nThe Administrator may adjust the patient match rate described in paragraph (1) if the Administrator determines that the patient match attestation rate should be adjusted to further incentivize the voluntary reporting of accurate patient match rates.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-03-26T16:57:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr2002",
          "measure-number": "2002",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2002v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Patient Matching And Transparency in Certified Health IT Act of 2025 or the MATCH IT Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a definition and standards for patient matching (i.e., the process of\u00a0accurately matching patients with their medical records, including when records are exchanged between health care providers). It also requires the development of\u00a0(1)\u00a0a minimum data set for technology standards\u00a0to increase patient matching, and (2) incentives for patient matching under Medicare.</p><p>Specifically, the bill requires HHS to develop a uniform definition and standards for patient matching to track patient match rates and document improvement over time. The definition and standards must account for certain situations, including duplicate records and multiple matches.</p><p>The bill also requires the Office of the National Coordinator for Health Information Technology (ONC) to adopt a minimum data set to help health care providers or health information systems achieve\u00a0a patient match rate of 99.9%. The\u00a0minimum data set and related standards must be incorporated\u00a0into the U.S. Core Data for Interoperability and the Medicare Promoting Interoperability Program\u00a0for\u00a0health information technology. </p><p>Additionally, the Centers for Medicare &\u00a0Medicaid Services (CMS) must\u00a0establish a voluntary bonus measure within the Medicare Promoting Interoperability Program to allow\u00a0health care providers who have a patient match rate over a certain percentage to receive a payment adjustment.\u00a0The ONC and CMS\u00a0must develop a voluntary reporting program for providers to anonymously submit patient matching data to HHS.\u00a0</p>"
        },
        "title": "MATCH IT Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2002.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Patient Matching And Transparency in Certified Health IT Act of 2025 or the MATCH IT Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a definition and standards for patient matching (i.e., the process of\u00a0accurately matching patients with their medical records, including when records are exchanged between health care providers). It also requires the development of\u00a0(1)\u00a0a minimum data set for technology standards\u00a0to increase patient matching, and (2) incentives for patient matching under Medicare.</p><p>Specifically, the bill requires HHS to develop a uniform definition and standards for patient matching to track patient match rates and document improvement over time. The definition and standards must account for certain situations, including duplicate records and multiple matches.</p><p>The bill also requires the Office of the National Coordinator for Health Information Technology (ONC) to adopt a minimum data set to help health care providers or health information systems achieve\u00a0a patient match rate of 99.9%. The\u00a0minimum data set and related standards must be incorporated\u00a0into the U.S. Core Data for Interoperability and the Medicare Promoting Interoperability Program\u00a0for\u00a0health information technology. </p><p>Additionally, the Centers for Medicare &\u00a0Medicaid Services (CMS) must\u00a0establish a voluntary bonus measure within the Medicare Promoting Interoperability Program to allow\u00a0health care providers who have a patient match rate over a certain percentage to receive a payment adjustment.\u00a0The ONC and CMS\u00a0must develop a voluntary reporting program for providers to anonymously submit patient matching data to HHS.\u00a0</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr2002"
    },
    "title": "MATCH IT Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Patient Matching And Transparency in Certified Health IT Act of 2025 or the MATCH IT Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to establish a definition and standards for patient matching (i.e., the process of\u00a0accurately matching patients with their medical records, including when records are exchanged between health care providers). It also requires the development of\u00a0(1)\u00a0a minimum data set for technology standards\u00a0to increase patient matching, and (2) incentives for patient matching under Medicare.</p><p>Specifically, the bill requires HHS to develop a uniform definition and standards for patient matching to track patient match rates and document improvement over time. The definition and standards must account for certain situations, including duplicate records and multiple matches.</p><p>The bill also requires the Office of the National Coordinator for Health Information Technology (ONC) to adopt a minimum data set to help health care providers or health information systems achieve\u00a0a patient match rate of 99.9%. The\u00a0minimum data set and related standards must be incorporated\u00a0into the U.S. Core Data for Interoperability and the Medicare Promoting Interoperability Program\u00a0for\u00a0health information technology. </p><p>Additionally, the Centers for Medicare &\u00a0Medicaid Services (CMS) must\u00a0establish a voluntary bonus measure within the Medicare Promoting Interoperability Program to allow\u00a0health care providers who have a patient match rate over a certain percentage to receive a payment adjustment.\u00a0The ONC and CMS\u00a0must develop a voluntary reporting program for providers to anonymously submit patient matching data to HHS.\u00a0</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119hr2002"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2002ih.xml"
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
      "title": "MATCH IT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:00Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MATCH IT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Patient Matching And Transparency in Certified Health IT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXX of the Public Health Service Act to establish standards and protocols to improve patient matching.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:36Z"
    }
  ]
}
```
