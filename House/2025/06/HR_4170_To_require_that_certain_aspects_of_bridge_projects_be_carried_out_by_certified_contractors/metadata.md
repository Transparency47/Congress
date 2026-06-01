# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4170?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4170
- Title: Bridge Corrosion Prevention and Repair Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4170
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-04-28T08:06:07Z
- Update date including text: 2026-04-28T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-26 - IntroReferral: Sponsor introductory remarks on measure. (CR E627)
- 2025-06-27 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-26 - IntroReferral: Sponsor introductory remarks on measure. (CR E627)
- 2025-06-27 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4170",
    "number": "4170",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000559",
        "district": "8",
        "firstName": "John",
        "fullName": "Rep. Garamendi, John [D-CA-8]",
        "lastName": "Garamendi",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Bridge Corrosion Prevention and Repair Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:07Z",
    "updateDateIncludingText": "2026-04-28T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E627)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-27T16:56:59Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
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
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MD"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NJ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4170ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4170\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Garamendi (for himself, Mr. Bost , Mr. Deluzio , Mr. Fitzpatrick , Ms. Brownley , Mr. Krishnamoorthi , Mr. Gottheimer , and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require that certain aspects of bridge projects be carried out by certified contractors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bridge Corrosion Prevention and Repair Act of 2025 .\n#### 2. Corrosion prevention for bridges\n##### (a) Definitions\nIn this section:\n**(1) Applicable bridge project**\nThe term applicable bridge project means a project for construction, replacement, rehabilitation, preservation, or protection, other than de minimis work, as determined by the entity carrying out the project, on\u2014\n**(A)**\na bridge project that receives financial assistance under title 23, United States Code; or\n**(B)**\na project for a railroad bridge (as defined in section 237.5 of title 49, Code of Federal Regulations (or successor regulations)) that receives financial assistance under title 49, United States Code.\n**(2) Certified contractor**\nThe term certified contractor means a contracting or subcontracting firm that has been certified by a third-party organization recognized industry-wide that evaluates the capability of the contractor or subcontractor to properly perform 1 or more specified aspects of an applicable bridge project described in subsection (b)(2).\n**(3) Qualified training program**\nThe term qualified training program means a training program in corrosion control, mitigation, and prevention that is\u2014\n**(A)**\noffered by an organization that provides trainees with a certification that meets the ANSI/NACE Number 13/SSPC\u2013ACS\u20131 standard (or a successor standard) or another standard approved by the Administrator of the Federal Highway Administration; or\n**(B)**\nan industrial coatings applicator training program\u2014\n**(i)**\nregistered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ) (50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ); and\n**(ii)**\nthat meets the standards of subpart A of part 29 and part 30 of title 29, Code of Federal Regulations (or successor regulations).\n##### (b) Applicable bridge projects\n**(1) Quality control**\nA certified contractor shall carry out aspects of an applicable bridge project described in paragraph (2).\n**(2) Aspects of applicable bridge projects**\nAspects of an applicable bridge project referred to in paragraph (1) include\u2014\n**(A)**\nsurface preparation or coating application on steel, concrete, or rebar of an applicable bridge project;\n**(B)**\nremoval of a lead-based or other hazardous coating from steel or concrete of an existing applicable bridge project; and\n**(C)**\nshop painting of structural steel or rebar fabricated for installation on an applicable bridge project.\n**(3) Corrosion management system**\nIn carrying out an applicable bridge project, the entity carrying out the project shall\u2014\n**(A)**\nimplement a corrosion management system that utilizes industry-recognized standards and corrosion mitigation and prevention methods to address different considerations, including\u2014\n**(i)**\nsurface preparation;\n**(ii)**\nprotective coatings;\n**(iii)**\nmaterials selection;\n**(iv)**\ncathodic protection;\n**(v)**\ncorrosion engineering;\n**(vi)**\npersonnel training; and\n**(vii)**\nbest practices in environmental protection to prevent environmental degradation and uphold public health; and\n**(B)**\nrequire certified contractors, for the purpose of carrying out aspects of applicable bridge projects described in paragraph (2), to employ a substantial number of individuals that are trained and certified by a qualified training program.\n**(4) Certification**\nFor an applicable bridge project that includes an aspect described in paragraph (2), the entity carrying out the project shall only accept bids from a certified contractor that presents written proof that the certification of the contractor meets the relevant (AMPP) SSPC\u2013QP standards (or a successor standard).\n##### (c) Training program\nAs a condition of entering into a contract for an applicable bridge project, each certified contractor shall provide training for each individual who is not a certified coating applicator but that the certified contractor employs to carry out aspects of applicable bridge projects described in subsection (b)(2).\n#### 3. Availability of Federal grant funding for corrosion control work on rail bridges\nSection 22402(b)(1) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (E), by striking or at the end;\n**(2)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(3)**\nby inserting after subparagraph (E) the following:\n(F) to perform corrosion control work on rail bridges; or .\n#### 4. Study on efficacy of weathering steel\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nweathering steel is often used for bridge construction projects because of its ability to withstand weather conditions better than other forms of steel;\n**(2)**\nthe collapse of the Fern Hollow Bridge in Pittsburgh, Pennsylvania, in January 2022 highlights the real threat that corrosion poses to the bridges of the United States;\n**(3)**\nmore research is needed into the vulnerabilities of weathering steel; and\n**(4)**\nStates and units of local government need more information on when and how to address the risk of corrosion to weathering steel.\n##### (b) Study\nNot later than 18 months after the date of enactment of this Act, the Secretary of Transportation shall\u2014\n**(1)**\ncarry out a study on best practices for\u2014\n**(A)**\nthe frequency and method of inspecting corrosion on weathering steel bridges; and\n**(B)**\naddressing corrosion on weathering steel bridges;\n**(2)**\nsubmit to the Committee on Environment and Public Works of the Senate, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Transportation and Infrastructure of the House of Representatives a report on the results of the study under paragraph (1); and\n**(3)**\nmake the report under paragraph (2) available to State departments of transportation, metropolitan planning organizations (as defined in section 134(b) of title 23, United States Code), regional transportation planning organizations (as defined in that section), and units of local government that own bridge assets.",
      "versionDate": "2025-06-26",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-16T13:20:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119hr4170",
          "measure-number": "4170",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-26",
          "originChamber": "HOUSE",
          "update-date": "2025-12-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4170v00",
            "update-date": "2025-12-16"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bridge Corrosion Prevention and Repair Act of 2025<strong></strong></strong></p><p>This bill establishes certain requirements to address corrosion control in bridge and railroad-bridge projects that receive federal assistance.</p><p>Specifically, certified contractors must employ a substantial number of individuals who are certified by a qualified training program in corrosion control, mitigation, and prevention in order to work on certain aspects of bridge project activities. A certified contractor must also provide training for any non-certified coating applicators employed by the contractor to work on certain aspects of a project.</p><p>The bill further requires bridge projects to implement a corrosion management system that utilizes industry-recognized standards and corrosion mitigation and prevention methods for construction, repair, and maintenance projects.</p><p>In addition, the bill expands the scope of the Railroad Rehabilitation and Improvement Financing Program to include corrosion control work on rail bridges. (This program provides direct loans and loan guarantees for the development of railroad infrastructure.)</p><p>The bill also requires the Department of Transportation to study and report on best practices for inspecting and addressing corrosion on weathering steel bridges. This report must be made available to state and local governments, metropolitan planning organizations, and regional organizations.</p>"
        },
        "title": "Bridge Corrosion Prevention and Repair Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4170.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bridge Corrosion Prevention and Repair Act of 2025<strong></strong></strong></p><p>This bill establishes certain requirements to address corrosion control in bridge and railroad-bridge projects that receive federal assistance.</p><p>Specifically, certified contractors must employ a substantial number of individuals who are certified by a qualified training program in corrosion control, mitigation, and prevention in order to work on certain aspects of bridge project activities. A certified contractor must also provide training for any non-certified coating applicators employed by the contractor to work on certain aspects of a project.</p><p>The bill further requires bridge projects to implement a corrosion management system that utilizes industry-recognized standards and corrosion mitigation and prevention methods for construction, repair, and maintenance projects.</p><p>In addition, the bill expands the scope of the Railroad Rehabilitation and Improvement Financing Program to include corrosion control work on rail bridges. (This program provides direct loans and loan guarantees for the development of railroad infrastructure.)</p><p>The bill also requires the Department of Transportation to study and report on best practices for inspecting and addressing corrosion on weathering steel bridges. This report must be made available to state and local governments, metropolitan planning organizations, and regional organizations.</p>",
      "updateDate": "2025-12-16",
      "versionCode": "id119hr4170"
    },
    "title": "Bridge Corrosion Prevention and Repair Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bridge Corrosion Prevention and Repair Act of 2025<strong></strong></strong></p><p>This bill establishes certain requirements to address corrosion control in bridge and railroad-bridge projects that receive federal assistance.</p><p>Specifically, certified contractors must employ a substantial number of individuals who are certified by a qualified training program in corrosion control, mitigation, and prevention in order to work on certain aspects of bridge project activities. A certified contractor must also provide training for any non-certified coating applicators employed by the contractor to work on certain aspects of a project.</p><p>The bill further requires bridge projects to implement a corrosion management system that utilizes industry-recognized standards and corrosion mitigation and prevention methods for construction, repair, and maintenance projects.</p><p>In addition, the bill expands the scope of the Railroad Rehabilitation and Improvement Financing Program to include corrosion control work on rail bridges. (This program provides direct loans and loan guarantees for the development of railroad infrastructure.)</p><p>The bill also requires the Department of Transportation to study and report on best practices for inspecting and addressing corrosion on weathering steel bridges. This report must be made available to state and local governments, metropolitan planning organizations, and regional organizations.</p>",
      "updateDate": "2025-12-16",
      "versionCode": "id119hr4170"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4170ih.xml"
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
      "title": "Bridge Corrosion Prevention and Repair Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bridge Corrosion Prevention and Repair Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that certain aspects of bridge projects be carried out by certified contractors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:33Z"
    }
  ]
}
```
