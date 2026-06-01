# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/880?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/880
- Title: Household Goods Shipping Consumer Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 880
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-03-12T12:50:22Z
- Update date including text: 2026-03-12T12:50:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-31 - IntroReferral: Sponsor introductory remarks on measure. (CR E80-81)
- 2025-02-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-31 - IntroReferral: Sponsor introductory remarks on measure. (CR E80-81)
- 2025-02-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/880",
    "number": "880",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Household Goods Shipping Consumer Protection Act",
    "type": "HR",
    "updateDate": "2026-03-12T12:50:22Z",
    "updateDateIncludingText": "2026-03-12T12:50:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
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
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E80-81)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:45:05Z",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MS"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "LA"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AR"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MS"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NM"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "KS"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
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
      "sponsorshipDate": "2025-05-29",
      "state": "AL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "FL"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AR"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NH"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "WI"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr880ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 880\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Norton (for herself, Mr. Ezell , Ms. Brownley , Mr. Carter of Louisiana , Mr. Hill of Arkansas , Mr. Garamendi , Mr. Cuellar , Ms. Scholten , and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nA bill to amend title 49, United States Code, to clarify the authority of the Administrator of the Federal Motor Carrier Safety Administration relating to the shipping of household goods, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Household Goods Shipping Consumer Protection Act .\n#### 2. Administrative Assessment of Civil Penalties for Violations of Commercial Regulations\n##### (a) Enforcement by Secretary\nSection 14914 of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (b), (c), and (d) as subsections (c), (d), and (e), respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Enforcement by Secretary If, after notice and an opportunity for a hearing, the Secretary finds that a person violated a provision of part B of subtitle IV of this title, or a regulation or order issued pursuant to such part, the Secretary shall assess a civil penalty by written notice. ;\n**(3)**\nin subsection (c), as redesignated by paragraph (1), by inserting or the Secretary after Board ; and\n**(4)**\nin subsection (d), as redesignated by paragraph (1), by inserting or the Secretary after Board .\n##### (b) Application\nSection 501(b) of title 49, United States Code, is amended\u2014\n**(1)**\nby inserting 5, after 20303 and chapters ; and\n**(2)**\nby inserting 311, 313, after chapters), .\n#### 3. State Use of Grant Funds for Commercial Enforcement and Consumer Protection\nSection 31102 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (1)(B), by striking and at the end;\n**(B)**\nin paragraph (2)(B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) for the enforcement of Federal household goods statutes and regulations for the interstate transportation of household goods by household goods motor carriers and brokers, and for the intrastate transportation of household goods by household goods motor carriers if the State has adopted laws or regulations that are compatible with Federal household goods regulations. ;\n**(2)**\nin subsection (l)(2)\u2014\n**(A)**\nin subparagraph (I), by striking and at the end;\n**(B)**\nby redesignating subparagraph (J) as subparagraph (K); and\n**(C)**\nby inserting after subparagraph (I) the following:\n(J) enforce Federal household goods statutes and regulations for the interstate transportation of household goods by household goods motor carriers and brokers, and for the intrastate transportation of household goods by household goods motor carriers if the State has adopted laws or regulations that are compatible with Federal household goods regulations; and ; and\n**(3)**\nby adding at the end the following:\n(m) State discretion The activities described in subsections (h)(3) and (l)(2)(J) are\u2014 (1) optional at the discretion of a State; and (2) not a condition on funds received under this section. .\n#### 4. State Retention of Penalties and Fines\nSection 14711 of title 49, United States Code, is amended by adding at the end the following:\n(g) Penalties Notwithstanding any other provision of law, any fine or penalty imposed on a carrier or broker in a proceeding under this section shall be paid to, and retained by, the State that imposed such fine or penalty. .\n#### 5. Registration Requirements\n##### (a) Definitions\nSection 13102 of title 49, United States Code, is amended by adding at the end the following:\n(28) Principal place of business The term principal place of business means a single physical business location of a specified entity where\u2014 (A) management officials of such specified entity report to work; (B) such specified entity conducts a significant portion of its business relating to the transportation of persons or property; and (C) such specified entity maintains records required by part B of subtitle IV or part B of subtitle VI. (29) Specified entity The term specified entity means\u2014 (A) an employer, as such term is defined in section 31132; (B) a person; (C) a motor carrier, including a foreign motor carrier or foreign motor private carrier; (D) a broker; or (E) a freight forwarder. .\n##### (b) Motor Carrier Generally\nSection 13902(a)(1) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C), by striking and at the end;\n**(2)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(E) has designated a principal place of business. .\n##### (c) Registration of freight forwarders\nSection 13903(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(3) has designated a principal place of business; and (4) has disclosed any relationship involving common ownership, common management, common control, or common familial relationship between such person and any other motor carrier, freight forwarder, broker, or any other applicant for motor carrier, freight forwarder, or broker registration, if the relationship occurred in the 3-year period preceding the date of the filing of the application for registration. .\n##### (d) Registration of brokers\nSection 13904(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (1) by striking and after the semicolon;\n**(2)**\nin subsection (2) by striking the period and inserting a semicolon; and\n**(3)**\nby inserting at the end the following:\n(3) has designated a principal place of business; and (4) has disclosed any relationship involving common ownership, common management, common control, or common familial relationship between such person and any other motor carrier, freight forwarder, or broker, or any other applicant for motor carrier, freight forwarder, or broker registration, if the relationship occurred in the 3-year period preceding the date of the filing of the application for registration. .\n##### (e) Complaints and actions on Secretary initiatives\nSection 13905(d)(2) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (C)(iii), by striking or at the end;\n**(2)**\nin subparagraph (D), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(E) withhold, suspend, amend, or revoke any part of a registration of a motor carrier, foreign motor carrier, foreign motor private carrier, broker, or freight forwarder if the Secretary finds that the motor carrier, foreign motor carrier, foreign motor private carrier, broker, or freight forwarder failed to designate a valid principal place of business. .\n##### (f) Requirement for registration and USDOT number\nSection 31134 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(4) the employer or person seeking registration has designated a principal place of business, as defined in section 13102. ; and\n**(2)**\nin subsection (c)(2), by striking subsection (b)(1) and inserting subsection (b) .",
      "versionDate": "2025-01-31",
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
        "actionDate": "2026-02-23",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 341."
      },
      "number": "337",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Household Goods Shipping Consumer Protection Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-11T18:31:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr880",
          "measure-number": "880",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2026-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr880v00",
            "update-date": "2026-03-12"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Household Goods Shipping Consumer Protection Act</strong></p><p>This bill allows the Federal Motor Carrier Safety Administration (FMCSA) to assess civil penalties against motor carriers, brokers, and freight forwarders for violations related to the interstate transportation of household goods and provides states with additional related authorities.</p><p>As background, a broker is the \u201cmiddle person\u201d between a shipper and a motor carrier and arranges for the transportation of household goods. A freight forwarder organizes shipments for individuals or corporations. Unlike a broker, freight forwarders assume responsibility for transportation and may transport the freight itself.</p><p>The bill expands the FMCSA registration requirements\u00a0to require motor carriers, brokers, and freight forwarders to designate a principal place of business (i.e., a single physical location where management officials report to work, a significant portion of the transportation\u00a0business is conducted, and records are maintained). FMCSA may withhold, suspend, amend, or revoke any part of a registration for failure to designate.</p><p>In addition,\u00a0brokers and freight forwarders must disclose any common ownership, management, control, or familial relationship with\u00a0any other carrier, freight forwarder, broker, or applicant in the previous three years. Under current law,\u00a0motor carriers must disclose this information.</p><p>Further, states may use certain grant funds to enforce federal household goods statutes and regulations for the interstate transportation of these goods by motor carriers and brokers.\u00a0This applies to Motor Carrier Safety Assistance Program (MCSAP) grant funds and MCSAP High Priority discretionary grant funds. A state shall retain collected fines that are a result of enforcement.</p>"
        },
        "title": "Household Goods Shipping Consumer Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr880.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Household Goods Shipping Consumer Protection Act</strong></p><p>This bill allows the Federal Motor Carrier Safety Administration (FMCSA) to assess civil penalties against motor carriers, brokers, and freight forwarders for violations related to the interstate transportation of household goods and provides states with additional related authorities.</p><p>As background, a broker is the \u201cmiddle person\u201d between a shipper and a motor carrier and arranges for the transportation of household goods. A freight forwarder organizes shipments for individuals or corporations. Unlike a broker, freight forwarders assume responsibility for transportation and may transport the freight itself.</p><p>The bill expands the FMCSA registration requirements\u00a0to require motor carriers, brokers, and freight forwarders to designate a principal place of business (i.e., a single physical location where management officials report to work, a significant portion of the transportation\u00a0business is conducted, and records are maintained). FMCSA may withhold, suspend, amend, or revoke any part of a registration for failure to designate.</p><p>In addition,\u00a0brokers and freight forwarders must disclose any common ownership, management, control, or familial relationship with\u00a0any other carrier, freight forwarder, broker, or applicant in the previous three years. Under current law,\u00a0motor carriers must disclose this information.</p><p>Further, states may use certain grant funds to enforce federal household goods statutes and regulations for the interstate transportation of these goods by motor carriers and brokers.\u00a0This applies to Motor Carrier Safety Assistance Program (MCSAP) grant funds and MCSAP High Priority discretionary grant funds. A state shall retain collected fines that are a result of enforcement.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hr880"
    },
    "title": "Household Goods Shipping Consumer Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Household Goods Shipping Consumer Protection Act</strong></p><p>This bill allows the Federal Motor Carrier Safety Administration (FMCSA) to assess civil penalties against motor carriers, brokers, and freight forwarders for violations related to the interstate transportation of household goods and provides states with additional related authorities.</p><p>As background, a broker is the \u201cmiddle person\u201d between a shipper and a motor carrier and arranges for the transportation of household goods. A freight forwarder organizes shipments for individuals or corporations. Unlike a broker, freight forwarders assume responsibility for transportation and may transport the freight itself.</p><p>The bill expands the FMCSA registration requirements\u00a0to require motor carriers, brokers, and freight forwarders to designate a principal place of business (i.e., a single physical location where management officials report to work, a significant portion of the transportation\u00a0business is conducted, and records are maintained). FMCSA may withhold, suspend, amend, or revoke any part of a registration for failure to designate.</p><p>In addition,\u00a0brokers and freight forwarders must disclose any common ownership, management, control, or familial relationship with\u00a0any other carrier, freight forwarder, broker, or applicant in the previous three years. Under current law,\u00a0motor carriers must disclose this information.</p><p>Further, states may use certain grant funds to enforce federal household goods statutes and regulations for the interstate transportation of these goods by motor carriers and brokers.\u00a0This applies to Motor Carrier Safety Assistance Program (MCSAP) grant funds and MCSAP High Priority discretionary grant funds. A state shall retain collected fines that are a result of enforcement.</p>",
      "updateDate": "2026-03-12",
      "versionCode": "id119hr880"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr880ih.xml"
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
      "title": "Household Goods Shipping Consumer Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-10T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Household Goods Shipping Consumer Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "A bill to amend title 49, United States Code, to clarify the authority of the Administrator of the Federal Motor Carrier Safety Administration relating to the shipping of household goods, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:33:35Z"
    }
  ]
}
```
