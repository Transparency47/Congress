# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3268
- Title: Broadband and Telecommunications RAIL Act
- Congress: 119
- Bill type: S
- Bill number: 3268
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-02-03T11:54:44Z
- Update date including text: 2026-02-03T11:54:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3268",
    "number": "3268",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Broadband and Telecommunications RAIL Act",
    "type": "S",
    "updateDate": "2026-02-03T11:54:44Z",
    "updateDateIncludingText": "2026-02-03T11:54:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T19:47:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3268is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3268\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Blackburn (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Communications Act of 1934 to streamline the deployment of telecommunications or broadband service facilities in public rights-of-way and the rights-of-way of railroad carriers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Broadband and Telecommunications RAIL Act .\n#### 2. Deployment of telecommunications or broadband service facilities in public rights-of-way and railroad rights-of-way\nTitle VII of the Communications Act of 1934 ( 47 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n723. Deployment of telecommunications or broadband service facilities in public rights-of-way and railroad rights-of- way (a) Definitions In this section: (1) Broadband service The term broadband service has the meaning given the term broadband internet access service in section 8.1(b) of title 47, Code of Federal Regulations (or any successor regulation). (2) Provider The term provider means a provider of telecommunications service or broadband service. (3) Public right-of-way The term public right-of-way means a public street, highway, route, or road (as designated by the Federal Government or a State or local government), including\u2014 (A) any railroad installation listed in the National Highway-Rail Crossing Inventory of the Department of Transportation as an over (at grade), under (subgrade), longitudinal (parallel), or transverse (crossing) installation; and (B) a private crossing with public access listed in the National Highway-Rail Crossing Inventory of the Department of Transportation. (4) Railroad carrier The term railroad carrier has the meaning given the term in section 20102 of title 49, United States Code. (5) Telecommunications or broadband service facility The term telecommunications or broadband service facility \u2014 (A) means a facility used to provide or support the provision of any telecommunications service or broadband service; and (B) includes a facility described in subparagraph (A) that is used to provide, or support the provision of, other services. (b) Notification of work by providers in public rights-of-Way (1) In general If a State or local government has authorized a provider to place or modify a telecommunications or broadband service facility in a public right-of-way, and the telecommunications or broadband service facility will be placed or modified in an area where the public right-of-way intersects with a railroad corridor, the provider\u2014 (A) shall submit to the applicable railroad carrier a written notification that the placement or modification has been authorized by the State or local government; and (B) shall not be required to submit an application to the railroad carrier under subsection (c) with respect to the placement or modification. (2) Contents A notification submitted under paragraph (1) shall contain the following information with respect to a placement or modification described in that paragraph: (A) The location of the placement or modification. (B) The proposed date of commencement of work with respect to the placement or modification. (C) The anticipated duration of the work described in subparagraph (B). (D) The entry and exit points that will be used with respect to the performance of the work described in subparagraph (B). (E) The contact information of the provider. (3) Scheduling Following the submission of a complete notification under paragraph (1) by a provider\u2014 (A) the provider shall schedule a date in coordination with the applicable railroad carrier for the placement or modification of the telecommunications or broadband service facility to which the notification applies; and (B) the placement or modification described in subparagraph (A) shall commence\u2014 (i) not earlier than the date that is 15 days after the date on which the notification is submitted; and (ii) not later than\u2014 (I) the date that is 30 days after the date on which the notification is submitted; or (II) such other date as mutually agreed upon by the provider and the applicable railroad carrier. (4) Payment not required (A) In general A provider shall not be required to pay a railroad carrier with respect to the placement or modification of a telecommunications or broadband service facility in a public right-of-way, as authorized by a State or local government. (B) Rule of construction Nothing in subparagraph (A) may be construed to affect any requirement, pursuant to an authorization by a State or local government for a provider to place or modify a telecommunications or broadband service facility in a public right-of- way, for the provider to make any payment to any entity with respect to the placement or modification. (c) Application To place or modify telecommunications or broadband service facilities in railroad rights-of-Way (1) In general In order to place or modify a telecommunications or broadband service facility in the right-of-way of a railroad carrier, a provider shall submit to the railroad carrier a written application that contains the following information: (A) Engineering design plans, construction plans, and (if applicable) bore plans with respect to the placement or modification. (B) The location of the placement or modification. (C) The proposed date of commencement of work with respect to the placement or modification. (D) The anticipated duration of the work described in subparagraph (C). (E) The entry and exit points that will be used with respect to the performance of the work described in subparagraph (C). (F) The contact information of the provider. (2) Decision (A) In general Not later than 60 days after the date on which a railroad carrier receives a complete application that contains the information required under paragraph (1), the railroad carrier shall\u2014 (i) approve or deny the application; and (ii) transmit to the provider that submitted the application a notification of the approval or denial under clause (i). (B) Exclusive reasons for denial A railroad carrier may only deny an application under subparagraph (A) if the placement or modification of a telecommunications or broadband service facility proposed in the application would\u2014 (i) substantially interfere with or damage the infrastructure or permanent operations of the railroad carrier; or (ii) jeopardize the safety of passengers or employees of the railroad carrier. (C) Explanation If a railroad carrier denies an application under subparagraph (A), the railroad carrier shall include in the notification required under clause (ii) of that subparagraph an identification of each reason under subparagraph (B) for which the railroad carrier denied the application and an explanation of how that reason for denial applies to the application. (3) Scheduling Following approval of an application under this subsection, the applicable provider shall schedule a date in coordination with the railroad carrier for the placement or modification of the applicable telecommunications or broadband service facility, which shall commence not later than\u2014 (A) the date that is 30 days after the date of the approval; or (B) such other date as indicated in the application or mutually agreed upon by the provider and the railroad carrier. (4) Compensation A provider that submits to a railroad carrier an application under this subsection shall pay the railroad carrier compensation in an amount that is equal to the actual costs reasonably and directly incurred by the railroad carrier with respect to the application. (d) Petition for relief (1) In general (A) Railroad carrier A railroad carrier may petition the Commission for relief regarding the placement or modification by a provider of a telecommunications or broadband service facility in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of the railroad carrier, if the railroad carrier asserts that\u2014 (i) in the case of a placement or modification with respect to which the provider has submitted an application to the railroad carrier under subsection (c), the amount of compensation that the provider proposes to pay under paragraph (4) of that subsection is not actual costs reasonably and directly incurred by the railroad carrier, as required by that paragraph; or (ii) the provider has otherwise failed to comply with this section or a regulation promulgated under this section. (B) Provider (i) In general A provider may petition the Commission for relief regarding the placement or modification by the provider of a telecommunications or broadband service facility in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, if the provider asserts that the relevant railroad carrier has\u2014 (I) wrongfully obstructed or delayed the placement or modification; (II) requested payment in an amount in excess of the actual costs required under subsection (c)(4); or (III) otherwise failed to comply with this section or a regulation promulgated under this section. (ii) Timing In the case of a placement or modification with respect to which a provider has submitted an application to a railroad carrier under subsection (c), the provider may not file a petition for relief under clause (i) with respect to the placement or modification before the earlier of\u2014 (I) the date on which the railroad carrier notifies the provider of the approval or denial of the application; and (II) the day after the date that is 60 days after the date on which the railroad carrier receives the application. (2) Adjudication (A) Jurisdiction The Commission shall be the sole Federal agency with jurisdiction to hear and resolve a petition filed under paragraph (1). (B) Findings In adjudicating a petition filed under paragraph (1), the Commission may make any necessary findings of fact or determinations. (C) Use of experts (i) In general In adjudicating a petition filed under paragraph (1), the Commission may employ experts to advise the Commission with respect to\u2014 (I) examining locations, plans, specifications, and descriptions of equipment and methods proposed to be employed; (II) hearing any objections and considering any modifications that the applicable railroad carrier or provider submits; (III) rejecting, approving, or modifying proposed plans and specifications; and (IV) technical, economic, and other matters concerning the applicable placement or modification. (ii) Reimbursement The party against which the Commission rules on an issue with respect to which an expert employed by the Commission under clause (i) renders services under that clause shall reimburse the Commission for the cost of those services. (iii) Deposit of collections Amounts received to reimburse the Commission for the cost of services rendered by an expert employed under clause (i) shall be deposited in, and credited to, the account through which funds were made available to pay that cost. (iv) Authority The Commission may employ experts under clause (i) pursuant to section 3109(b) of title 5, United States Code. (D) Coordination with Federal agencies In adjudicating a petition filed under paragraph (1), the Commission shall coordinate with the Administrator of the Federal Railroad Administration regarding any finding of fact or determination relating to railroad safety. (E) Final order (i) In general Not later than 90 days after the date on which a petition is filed under paragraph (1), the Commission shall issue a final order regarding the petition in which the Commission may grant such relief as the Commission considers appropriate. (ii) Extension of deadline (I) In general Except as provided in subclause (II), the Commission may extend the deadline with respect to a petition under clause (i), as the Commission considers appropriate. (II) Exception The Commission may not extend the deadline with respect to a petition under clause (i) on the basis of the coordination required under subparagraph (D). (e) Responsibilities of parties (1) Railroad carriers With respect to the placement or modification by a provider of a telecommunications or broadband service facility in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, the relevant railroad carrier shall\u2014 (A) take such protective measures as the railroad carrier determines necessary and appropriate; and (B) perform any work necessary to implement the placement or modification that the provider is prohibited from performing because of the limitations under subsection (f)(2)(D). (2) Providers With respect to the placement or modification by a provider of a telecommunications or broadband service facility in an area where a public right-of-way intersects with a railroad corridor, or in the right-of-way of a railroad carrier, the provider\u2014 (A) shall not be required to obtain additional insurance for the placement or modification; and (B) shall\u2014 (i) carry out all aspects of the implementation of the placement or modification (other than any work necessary to implement the placement or modification that the provider is prohibited from performing because of the limitations under subsection (f)(2)(D)); and (ii) ensure that the placement or modification is carried out, and that the telecommunications or broadband service facility is operated, in accordance with\u2014 (I) all applicable Federal laws and regulations, including those relating to railroad safety; and (II) any accepted industry standards specified by the Commission. (f) Rulemaking (1) In general Not later than 1 year after the date of enactment of this section, the Commission shall promulgate regulations (which may include regulations applicable to railroad carriers) to implement this section in a manner that\u2014 (A) ensures railroad safety, including by ensuring compliance with all applicable Federal laws and regulations, including those relating to railroad safety; (B) provides a process for more the timely placement or modification of a telecommunications or broadband service facility in an emergency situation than would otherwise be provided for under this section; (C) prevents substantial interference with the infrastructure or operations of railroad carriers; (D) allows for the timely and efficient placement and modification of telecommunications or broadband service facilities; and (E) provides a process for the more timely placement or modification of a telecommunications or broadband service facility in a railroad carrier crossing that is discontinued or abandoned than would otherwise be provided for under this section. (2) Matters to be included In the regulations promulgated under paragraph (1), the Commission shall\u2014 (A) establish standards and procedures for determining whether the reasons for denial under clauses (i) and (ii) of subsection (c)(2)(B) are satisfied; (B) establish standards and procedures for determining actual costs under subsection (c)(4); (C) establish standards and procedures for adjudicating petitions for relief under subsection (d), including with respect to reimbursement of the Commission for the cost of services rendered by experts employed under subsection (d)(2)(C); (D) specify any limitations on the locations within an area where a public right-of-way intersects with a railroad corridor, or within the right-of-way of a railroad carrier, where a provider may perform work relating to the placement or modification of a telecommunications or broadband service facility, or on the types of such work that a provider may perform within such an area or right-of-way, in order to ensure railroad safety and to prevent substantial interference with the infrastructure or operations of railroad carriers; and (E) otherwise establish standards and procedures and define terms as necessary to implement this section. (3) Coordination with Federal agencies In promulgating regulations under paragraph (1), the Commission shall coordinate with the Administrator of the Federal Railroad Administration regarding any matter relating to railroad safety. (g) Memorandum of understanding Not later than 60 days after the date of enactment of this section, the Commission and the Administrator of the Federal Railroad Administration shall confer and enter into a memorandum of understanding to work cooperatively to ensure that safety concerns of railroad carriers and users of public rights-of-way are addressed in any coordination that occurs pursuant to subsection (d)(2)(D) or (f)(3). (h) Rule of construction Nothing in this section, including in any regulation promulgated under subsection (f), may be construed as establishing, eliminating, or modifying an agreement between a railroad carrier and a labor organization representing a class or craft of employees of that railroad carrier that is covered by the Railway Labor Act ( 45 U.S.C. 151 et seq. ). .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-12-03",
        "text": "Ordered to be Reported by the Yeas and Nays: 51 - 0."
      },
      "number": "6046",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Broadband and Telecommunications RAIL Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-06T19:26:44Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3268is.xml"
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
      "title": "Broadband and Telecommunications RAIL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-20T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Broadband and Telecommunications RAIL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Communications Act of 1934 to streamline the deployment of telecommunications or broadband service facilities in public rights-of-way and the rights-of-way of railroad carriers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:27Z"
    }
  ]
}
```
