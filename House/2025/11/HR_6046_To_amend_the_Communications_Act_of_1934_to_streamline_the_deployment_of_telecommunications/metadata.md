# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6046?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6046
- Title: Broadband and Telecommunications RAIL Act
- Congress: 119
- Bill type: HR
- Bill number: 6046
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-02-03T13:55:28Z
- Update date including text: 2026-02-03T13:55:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-17 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2025-11-18 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-11-18 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 51 - 0.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-17 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2025-11-18 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-11-18 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 51 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6046",
    "number": "6046",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Broadband and Telecommunications RAIL Act",
    "type": "HR",
    "updateDate": "2026-02-03T13:55:28Z",
    "updateDateIncludingText": "2026-02-03T13:55:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 51 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Communications and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
        "item": [
          {
            "date": "2025-12-03T21:52:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-17T17:00:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-18T17:17:15Z",
                "name": "Reported by"
              },
              {
                "date": "2025-11-18T17:16:49Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-17T17:16:27Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "OH"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6046ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6046\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Joyce of Pennsylvania (for himself, Mr. Landsman , and Mr. Peters ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to streamline the deployment of telecommunications or broadband service facilities in the public rights-of-way and the rights-of-way of railroad carriers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Broadband and Telecommunications RAIL Act .\n#### 2. Deployment of telecommunications or broadband service facilities in public rights-of-way and railroad rights-of-way\nTitle VII of the Communications Act of 1934 ( 47 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n723. Deployment of telecommunications or broadband service facilities in public rights-of-way and railroad rights-of-way (a) Notification of work by providers in public rights-of-Way (1) In general If a State or local government has authorized a provider to place or modify telecommunications or broadband service facilities in a public right-of-way, and the facilities will be placed or modified in an area where the public right-of-way intersects with a railroad corridor, the provider\u2014 (A) shall submit to the relevant railroad carrier a written notification that the placement or modification has been authorized by the State or local government; and (B) is not required to submit an application to the railroad carrier under subsection (b) with respect to the placement or modification. (2) Contents A notification submitted under paragraph (1) shall contain the following information with respect to the placement or modification described in such paragraph: (A) The location of the placement or modification. (B) The proposed date of commencement of work with respect to the placement or modification. (C) The anticipated duration of the work. (D) The entry and exit points that will be used with respect to the performance of the work. (E) The contact information of the provider. (3) Scheduling Following the submission of a notification under paragraph (1)\u2014 (A) the provider shall schedule a date in coordination with the railroad carrier for the placement or modification of the facilities to which the notification applies; and (B) the placement or modification described in subparagraph (A) shall commence\u2014 (i) not earlier than the date that is 15 days after the date on which the notification is submitted; and (ii) not later than\u2014 (I) the date that is 30 days after the date on which the notification is submitted; or (II) such other date as mutually agreed upon by the provider and the railroad carrier. (4) Payment not required (A) In general A provider is not required to pay a railroad carrier with respect to the placement or modification of telecommunications or broadband service facilities in a public right-of-way as authorized by a State or local government. (B) Rule of construction Nothing in subparagraph (A) may be construed to affect any requirement, pursuant to an authorization by a State or local government for a provider to place or modify telecommunications or broadband service facilities in a public right-of-way, for the provider to make any payment to any entity with respect to the placement or modification. (b) Application To place or modify telecommunications or broadband service facilities in railroad rights-of-Way (1) In general In order to place or modify telecommunications or broadband service facilities in the right-of-way of a railroad carrier, a provider shall submit to the railroad carrier a written application that contains the following information: (A) Engineering design plans, construction plans, and (if applicable) bore plans with respect to the placement or modification. (B) The location of the placement or modification. (C) The proposed date of commencement of work with respect to the placement or modification. (D) The anticipated duration of the work. (E) The entry and exit points that will be used with respect to the performance of the work. (F) The contact information of the provider. (2) Decision (A) In general Not later than 60 days after the date on which a railroad carrier receives an application that contains the information required by paragraph (1), the railroad carrier shall\u2014 (i) approve or deny the application; and (ii) transmit to the provider that submitted the application a notification of the approval or denial under clause (i). (B) Exclusive reasons for denial A railroad carrier may only deny an application under subparagraph (A) if the placement or modification of telecommunications or broadband service facilities proposed in the application would\u2014 (i) substantially interfere with or damage the infrastructure of the railroad carrier; or (ii) jeopardize the safety of passengers or employees of the railroad carrier. (C) Explanation If a railroad carrier denies an application under subparagraph (A), the railroad carrier shall include in the notification required by clause (ii) of such subparagraph an identification of each reason described in subparagraph (B) for which the railroad carrier denied the application and an explanation of how such reason for denial applies to the application. (3) Scheduling Following approval of an application under this subsection, the provider shall schedule a date in coordination with the railroad carrier for the placement or modification of the facilities, which placement or modification shall commence not later than\u2014 (A) the date that is 30 days after the date of the approval; or (B) such other date as indicated in the application or mutually agreed upon by the provider and the railroad carrier. (4) Compensation A provider that submits to a railroad carrier an application under this subsection shall pay the railroad carrier compensation that is equal to the actual costs reasonably and directly incurred by the railroad carrier with respect to the application (including any placement or modification of telecommunications or broadband service facilities carried out pursuant to the application, to the extent such costs relate to railroad safety). (c) Petition for relief (1) In general (A) Railroad carrier A railroad carrier may petition the Commission for relief regarding the placement or modification by a provider of telecommunications or broadband service facilities in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of the railroad carrier, if the railroad carrier asserts that\u2014 (i) in the case of a placement or modification with respect to which the provider has submitted an application to the railroad carrier under subsection (b), the amount of compensation that the provider proposes to pay under paragraph (4) of such subsection is not actual costs as required by such paragraph; or (ii) the provider has otherwise failed to comply with this section or a regulation promulgated under this section. (B) Provider (i) In general A provider may petition the Commission for relief regarding the placement or modification by the provider of telecommunications or broadband service facilities in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, if the provider asserts that the relevant railroad carrier has\u2014 (I) wrongfully obstructed or delayed the placement or modification; (II) requested payment above actual costs required by subsection (b)(4); or (III) otherwise failed to comply with this section or a regulation promulgated under this section. (ii) Timing In the case of a placement or modification with respect to which a provider has submitted an application to a railroad carrier under subsection (b), the provider may not file a petition for relief under clause (i) with respect to the placement or modification before the earlier of\u2014 (I) the date on which the railroad carrier notifies the provider of the approval or denial of the application; and (II) the day after the date that is 60 days after the date on which the railroad carrier receives the application. (2) Adjudication (A) Jurisdiction The Commission shall be the sole Federal agency with jurisdiction to hear and resolve a petition filed under paragraph (1). (B) Findings In adjudicating a petition filed under paragraph (1), the Commission may make any necessary findings of fact or determinations. (C) Use of experts (i) In general In adjudicating a petition filed under paragraph (1), the Commission may employ experts to advise the Commission with respect to\u2014 (I) examining locations, plans, specifications, and descriptions of equipment and methods proposed to be employed; (II) hearing any objections and considering any modifications that the railroad carrier or provider submits; (III) rejecting, approving, or modifying proposed plans and specifications; and (IV) technical, economic, and other matters concerning the placement or modification. (ii) Reimbursement The party against which the Commission rules on an issue with respect to which an expert employed by the Commission under clause (i) renders services under such clause shall reimburse the Commission for the cost of such services. (iii) Deposit of collections Amounts received to reimburse the Commission for the cost of services rendered by an expert employed under clause (i) shall be deposited in, and credited to, the account through which funds were made available to pay such cost. (iv) Authority The Commission may employ experts under clause (i) pursuant to section 3109(b) of title 5, United States Code. (D) Coordination with Federal agencies In adjudicating a petition filed under paragraph (1), the Commission shall coordinate with the Administrator of the Federal Railroad Administration and the Surface Transportation Board regarding any finding of fact or determination relating to railroad safety. (E) Final order (i) In general Not later than 90 days after the date on which a petition is filed under paragraph (1), the Commission shall issue a final order regarding the petition in which the Commission may grant such relief as the Commission considers appropriate. (ii) Extension of deadline (I) In general Except as provided in subclause (II), the Commission may extend the deadline with respect to a petition under clause (i), as the Commission considers appropriate. (II) Exception The Commission may not extend the deadline with respect to a petition under clause (i) on the basis of the coordination required by subparagraph (D). (d) Responsibilities of parties (1) Railroad carriers With respect to the placement or modification by a provider of telecommunications or broadband service facilities in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, the relevant railroad carrier shall\u2014 (A) take such protective measures as the railroad carrier determines necessary and appropriate; and (B) perform any work necessary to implement the placement or modification that the provider is prohibited from performing because of the limitations specified under subsection (e)(2)(D). (2) Providers With respect to the placement or modification by a provider of telecommunications or broadband service facilities in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, the provider\u2014 (A) is not required to obtain additional insurance for the placement or modification; and (B) shall\u2014 (i) carry out all aspects of the implementation of the placement or modification (other than any work necessary to implement the placement or modification that the provider is prohibited from performing because of the limitations specified under subsection (e)(2)(D)); and (ii) ensure that the facilities are constructed and operated in accordance with\u2014 (I) all applicable Federal laws and regulations, including those relating to railroad safety; and (II) any accepted industry standards specified by the Commission. (e) Rulemaking (1) In general Not later than 1 year after the date of the enactment of this section, the Commission shall promulgate regulations (which may include regulations applicable to railroad carriers) to implement this section in a manner that\u2014 (A) ensures railroad safety, including by ensuring compliance with all applicable Federal laws and regulations, including those relating to railroad safety; (B) provides a process for more timely placement or modification of telecommunications or broadband service facilities in emergency situations than would otherwise be provided for under this section; (C) prevents substantial interference with the infrastructure or operations of railroad carriers; (D) allows for the timely and efficient placement and modification of telecommunications or broadband service facilities; and (E) provides a process for more timely placement or modification of telecommunications or broadband service facilities in railroad carrier crossings that are closed or abandoned than would otherwise be provided for under this section. (2) Matters to be included In the regulations promulgated under paragraph (1), the Commission shall\u2014 (A) establish standards and procedures for determining whether the reasons for denial under clauses (i) and (ii) of subsection (b)(2)(B) are met; (B) establish standards and procedures for determining actual costs under subsection (b)(4); (C) establish standards and procedures for adjudicating petitions for relief under subsection (c), including with respect to reimbursement of the Commission for the cost of services rendered by experts employed under subsection (c)(2)(C); (D) specify any limitations on the locations within an area where a public right-of-way intersects with a railroad corridor, or within the right-of-way of a railroad carrier, where a provider may perform work relating to the placement or modification of telecommunications or broadband service facilities, or on the types of such work that a provider may perform within such an area or right-of-way, in order to ensure railroad safety and to prevent substantial interference with the infrastructure or operations of railroad carriers; and (E) otherwise establish standards and procedures and define terms as necessary to implement this section. (3) Coordination with Federal agencies In promulgating regulations under paragraph (1), the Commission shall coordinate with the Administrator of the Federal Railroad Administration and the Surface Transportation Board regarding any matter relating to railroad safety. (f) Definitions In this section: (1) Broadband service The term broadband service has the meaning given the term broadband internet access service in section 8.1(b) of title 47, Code of Federal Regulations (or any successor regulation). (2) Provider The term provider means a provider of telecommunications service or broadband service. (3) Railroad carrier The term railroad carrier has the meaning given such term in section 20102 of title 49, United States Code. (4) Telecommunications or broadband service facilities The term telecommunications or broadband service facilities \u2014 (A) means facilities used to provide or support the provision of any telecommunications service or broadband service; and (B) includes facilities described in subparagraph (A) that are used to provide or support the provision of other services. .",
      "versionDate": "2025-11-17",
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
        "actionDate": "2025-11-20",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3268",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Broadband and Telecommunications RAIL Act",
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
            "name": "Advisory bodies",
            "updateDate": "2025-12-03T15:36:57Z"
          },
          {
            "name": "Industrial facilities",
            "updateDate": "2025-12-03T15:24:07Z"
          },
          {
            "name": "Infrastructure development",
            "updateDate": "2025-12-03T15:22:08Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-12-03T15:19:33Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-12-03T15:22:44Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-12-03T15:22:00Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-12-03T15:18:36Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-12-03T15:23:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-20T17:04:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-17",
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
          "measure-id": "id119hr6046",
          "measure-number": "6046",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-17",
          "originChamber": "HOUSE",
          "update-date": "2026-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6046v00",
            "update-date": "2026-02-03"
          },
          "action-date": "2025-11-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Broadband and Telecommunications RAIL Act</strong></p><p>This bill establishes a framework for the placement or modification of broadband or telecommunications equipment in a railroad corridor.</p><p>Specifically, if a broadband or telecommunications provider is seeking to place or modify equipment within a railroad carrier\u2019s right-of-way, the provider must submit an application to the carrier. A carrier must approve or deny an application within 60 days of receipt, and may only deny an application for safety reasons or if the placement or modification would substantially interfere with or damage railroad infrastructure. Once an application is approved, work must be scheduled in coordination with the carrier and generally must begin within 30 days. A provider must pay the railroad carrier for actual costs incurred with respect to the application.</p><p>However, if a provider has been authorized by a state or local government to place or modify equipment in a public right-of-way in an area that intersects with a railroad corridor, the provider need only notify the relevant railroad carrier and schedule the work in coordination with the carrier. Work must generally begin between 15 and 30 days after the notification is submitted. No fee is required.</p><p>A provider or carrier may petition the Federal Communications Commission (FCC) for relief if the other has failed to comply with these provisions.</p><p>The FCC must promulgate regulations to implement these provisions in a manner that ensures railroad safety, provides a timelier process for emergency situations, and prevents substantial interference with railroad infrastructure or operations, among other requirements.</p>"
        },
        "title": "Broadband and Telecommunications RAIL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6046.xml",
    "summary": {
      "actionDate": "2025-11-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband and Telecommunications RAIL Act</strong></p><p>This bill establishes a framework for the placement or modification of broadband or telecommunications equipment in a railroad corridor.</p><p>Specifically, if a broadband or telecommunications provider is seeking to place or modify equipment within a railroad carrier\u2019s right-of-way, the provider must submit an application to the carrier. A carrier must approve or deny an application within 60 days of receipt, and may only deny an application for safety reasons or if the placement or modification would substantially interfere with or damage railroad infrastructure. Once an application is approved, work must be scheduled in coordination with the carrier and generally must begin within 30 days. A provider must pay the railroad carrier for actual costs incurred with respect to the application.</p><p>However, if a provider has been authorized by a state or local government to place or modify equipment in a public right-of-way in an area that intersects with a railroad corridor, the provider need only notify the relevant railroad carrier and schedule the work in coordination with the carrier. Work must generally begin between 15 and 30 days after the notification is submitted. No fee is required.</p><p>A provider or carrier may petition the Federal Communications Commission (FCC) for relief if the other has failed to comply with these provisions.</p><p>The FCC must promulgate regulations to implement these provisions in a manner that ensures railroad safety, provides a timelier process for emergency situations, and prevents substantial interference with railroad infrastructure or operations, among other requirements.</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr6046"
    },
    "title": "Broadband and Telecommunications RAIL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband and Telecommunications RAIL Act</strong></p><p>This bill establishes a framework for the placement or modification of broadband or telecommunications equipment in a railroad corridor.</p><p>Specifically, if a broadband or telecommunications provider is seeking to place or modify equipment within a railroad carrier\u2019s right-of-way, the provider must submit an application to the carrier. A carrier must approve or deny an application within 60 days of receipt, and may only deny an application for safety reasons or if the placement or modification would substantially interfere with or damage railroad infrastructure. Once an application is approved, work must be scheduled in coordination with the carrier and generally must begin within 30 days. A provider must pay the railroad carrier for actual costs incurred with respect to the application.</p><p>However, if a provider has been authorized by a state or local government to place or modify equipment in a public right-of-way in an area that intersects with a railroad corridor, the provider need only notify the relevant railroad carrier and schedule the work in coordination with the carrier. Work must generally begin between 15 and 30 days after the notification is submitted. No fee is required.</p><p>A provider or carrier may petition the Federal Communications Commission (FCC) for relief if the other has failed to comply with these provisions.</p><p>The FCC must promulgate regulations to implement these provisions in a manner that ensures railroad safety, provides a timelier process for emergency situations, and prevents substantial interference with railroad infrastructure or operations, among other requirements.</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr6046"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6046ih.xml"
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
      "title": "Broadband and Telecommunications RAIL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadband and Telecommunications RAIL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to streamline the deployment of telecommunications or broadband service facilities in the public rights-of-way and the rights-of-way of railroad carriers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:21Z"
    }
  ]
}
```
