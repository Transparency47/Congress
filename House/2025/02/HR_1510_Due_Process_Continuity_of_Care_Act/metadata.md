# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1510
- Title: Due Process Continuity of Care Act
- Congress: 119
- Bill type: HR
- Bill number: 1510
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-04-16T08:06:58Z
- Update date including text: 2026-04-16T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-08 19:04:01 - Floor: ASSUMING FIRST SPONSORSHIP - Ms. Dexter asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 1510, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-08 19:04:01 - Floor: ASSUMING FIRST SPONSORSHIP - Ms. Dexter asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 1510, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1510",
    "number": "1510",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000489",
        "district": "18",
        "firstName": "Sylvester",
        "fullName": "Rep. Turner, Sylvester [D-TX-18]",
        "lastName": "Turner",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Due Process Continuity of Care Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:58Z",
    "updateDateIncludingText": "2026-04-16T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2025-09-08",
      "actionTime": "19:04:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Ms. Dexter asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 1510, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:35:30Z",
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
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "OH"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NE"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MN"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "WA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MI"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NM"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "WA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "VT"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "OH"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "VA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1510ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1510\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Turner of Texas (for himself, Mr. Turner of Ohio , Mr. Rutherford , Mr. Tonko , Mr. Bacon , Mr. Van Drew , Mr. Finstad , Mr. Obernolte , Mr. Doggett , Ms. Norton , Ms. Scanlon , Mr. Smith of Washington , Mr. Costa , Mr. Goldman of New York , Mr. Horsford , Ms. Crockett , Ms. Tlaib , Ms. Brownley , Ms. McCollum , Ms. Bonamici , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to remove the Medicaid coverage exclusion for inmates in custody pending disposition of charges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Due Process Continuity of Care Act .\n#### 2. Removal of inmate limitation on benefits under Medicaid\n##### (a) In general\nThe subdivision (A) of section 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) following the last numbered paragraph of such section is amended by inserting , or, at the option of the State, while in custody pending disposition of charges after patient in a medical institution .\n##### (b) Conforming Amendments\nSection 5122 of division FF of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ) is amended\u2014\n**(1)**\nin subsection (a), by striking \u201cMedicaid\u201d and all that follows through \u201cSection 1902(a)(84)(A)\u201d and inserting \u201c Medicaid .\u2014Section 1902(a)(84)(A)\u201d; and\n**(2)**\nin subsection (c), by inserting \u201c, except that if such date is later than the effective date described in section 2(c) of the Due Process Continuity of Care Act then the amendment made by subsection (a) shall take effect and apply to items and services furnished for periods beginning on or after the effective date described in such section\u201d before the period.\n##### (c) Effective date\nThe amendments made by subsections (a) and (b) shall take effect on the 1st day of the 1st calendar quarter that begins on or after the date that is 60 days after the date of the enactment of this Act and shall apply to items and services furnished for periods beginning on or after such date.\n#### 3. Planning grants\n##### (a) In general\nThe Secretary shall award planning grants to States to support providing medical assistance under the State Medicaid program to individuals who are eligible for such assistance as a result of the amendment made by section 2(a). The grants shall be used to prepare an application that meets the requirements of subsection (b).\n##### (b) Application requirements\nIn order to be awarded a planning grant under this section, a State shall submit an application to the Secretary at such time and in such form and manner as the Secretary shall require, that includes the following information along with such additional information, provisions, and assurances, as the Secretary may require:\n**(1)**\nA proposed process for carrying out each of the activities described in subsection (c) in the State.\n**(2)**\nA review of State policies regarding the population of individuals who are eligible for medical assistance under the State Medicaid program as a result of the amendment made by section 2(a) with respect to whether such policies may create barriers to increasing the number of health care providers who can provide items and services for that population.\n**(3)**\nThe development of a plan, taking into account activities described in subsection (c)(2), that will ensure a sustainable number of Medicaid-enrolled providers under the State Medicaid program that can offer a full array of treatment and services to the patient population described in paragraph (2) as needed. Such plan shall include the following:\n**(A)**\nSpecific activities to increase the number of providers that will offer physical health treatment, as well as services related to behavioral health treatment, including substance use disorder treatment, recovery, or support services (including short-term detoxification services, outpatient substance use disorder services, and evidence-based peer recovery services).\n**(B)**\nMilestones and timeliness for implementing activities set forth in the plan.\n**(C)**\nSpecific measurable targets for increasing the number of providers under the State Medicaid program who will treat the patient population described in paragraph (2).\n**(4)**\nAn assurance that the State consulted with relevant stakeholders, including the State agency responsible for administering the State Medicaid program, Medicaid managed care plans, health care providers, law enforcement personnel, officials from jails, and Medicaid beneficiary advocates, with respect to the preparation and completion of the application and a description of such consultation.\n##### (c) Activities described\nFor purposes of subsection (b)(1), the activities described in this subsection are the following:\n**(1)**\nActivities that support the development of an initial assessment of the health treatment needs of patients who are in custody pending disposition of charges to determine the extent to which providers are needed (including the types of such providers and geographic area of need) to improve the number of providers that will treat patients in custody pending disposition of charges under the State Medicaid program, including the following:\n**(A)**\nAn estimate of the number of individuals enrolled under the State Medicaid program who are in custody pending disposition of charges.\n**(B)**\nInformation on the capacity of providers to provide treatment or services to such individuals enrolled under the State Medicaid program, including information on providers who provide such services and their participation under the State Medicaid program.\n**(C)**\nInformation on the health care services provided under programs other than the State Medicaid program in jails to individuals who are in custody pending disposition of charges.\n**(2)**\nActivities that, taking into account the results of the assessment described in paragraph (1) with respect to the provision of treatment or services under the State Medicaid program, support the development of State infrastructure to recruit or contract with prospective health care providers, provide training and technical assistance to such providers, and secure a process for an electronic health record system for billing to reimburse for services provided by the correctional facility, outpatient providers, medical vendors, and contracted telehealth service providers to patients who are in custody pending disposition of charges that are compliant with applicable requirements and regulations for State Medicaid programs.\n**(3)**\nActivities that ensure the quality of care for patients who are in custody pending disposition of charges, including formal reporting mechanisms for patient outcomes, and activities that promote participation in learning collaboratives among providers treating this population.\n##### (d) Geographic diversity\nThe Secretary shall select States for planning grants under this section in a manner that ensures geographic diversity.\n##### (e) Funding\nThere are authorized to be appropriated $50,000,000 to carry out this section.\n##### (f) Definitions\nIn this section:\n**(1) Medicaid program**\nThe term Medicaid program means, with respect to a State, the State program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) including any waiver or demonstration under such title or under section 1115 of such Act ( 42 U.S.C. 1315 ) relating to such title.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(3) State**\nThe term State has the meaning given that term for purposes of title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) in section 1101(a)(1) of such Act ( 42 U.S.C. 1301(a)(1) ).",
      "versionDate": "2025-02-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-12",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1720",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Due Process Continuity of Care Act",
      "type": "S"
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
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-07-17T18:41:47Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-17T18:41:47Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-17T18:41:47Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-17T18:41:47Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-07-17T18:41:47Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-17T18:41:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T13:34:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1510",
          "measure-number": "1510",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1510v00",
            "update-date": "2025-03-26"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>"
        },
        "title": "Due Process Continuity of Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1510.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1510"
    },
    "title": "Due Process Continuity of Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>",
      "updateDate": "2025-03-26",
      "versionCode": "id119hr1510"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1510ih.xml"
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
      "title": "Due Process Continuity of Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Due Process Continuity of Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to remove the Medicaid coverage exclusion for inmates in custody pending disposition of charges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:27Z"
    }
  ]
}
```
