# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2366?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2366
- Title: American Families United Act
- Congress: 119
- Bill type: HR
- Bill number: 2366
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-04-23T08:07:07Z
- Update date including text: 2026-04-23T08:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2366",
    "number": "2366",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000299",
        "district": "16",
        "firstName": "Veronica",
        "fullName": "Rep. Escobar, Veronica [D-TX-16]",
        "lastName": "Escobar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "American Families United Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:07Z",
    "updateDateIncludingText": "2026-04-23T08:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
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
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-26",
      "state": "WA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NJ"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sponsorshipDate": "2025-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
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
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
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
      "sponsorshipDate": "2025-09-17",
      "state": "MN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NV"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "CO"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "TX"
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
      "sponsorshipDate": "2026-01-30",
      "state": "DC"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "GA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2366ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2366\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Ms. Escobar (for herself, Ms. Salazar , Mr. Tonko , Mr. Espaillat , Mr. Carbajal , Mr. Casar , Mr. Correa , Ms. Dean of Pennsylvania , Ms. DelBene , Mr. Garc\u00eda of Illinois , Mr. Menendez , Ms. Ross , Ms. Salinas , Ms. S\u00e1nchez , Ms. Scanlon , Mr. Soto , Mr. Suozzi , Ms. McCollum , Mr. Levin , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to promote family unity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Families United Act .\n#### 2. Rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto provide the Secretary of Homeland Security or the Attorney General with the ability to exercise the discretionary authority provided in this Act, or by an amendment made by this Act, except on a case-by-case basis; or\n**(2)**\nto otherwise modify or limit the discretionary authority of the Secretary of Homeland Security or the Attorney General under the immigration laws (as defined in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) )).\n#### 3. Discretionary authority with respect to family members of united states citizens\n##### (a) Applications for relief from removal\nSection 240(c)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(c)(4) ) is amended by adding at the end the following:\n(D) Judicial discretion (i) In general In the case of an alien who is the spouse or child of a citizen of the United States, the Attorney General may subject to clause (ii)\u2014 (I) terminate any removal proceedings against the alien; (II) decline to order the alien removed from the United States; (III) grant the alien permission to reapply for admission to the United States; or (IV) subject to clause (iii), waive the application of one or more grounds of inadmissibility or deportability in connection with any request for relief from removal. (ii) Limitation on discretion (I) In general The Attorney General may exercise the discretion described in clause (i) if the Attorney General determines that removal of the alien or the denial of a request for relief from removal would result in hardship to the alien\u2019s United States citizen spouse, parent, or child. There shall be a presumption that family separation constitutes hardship. (II) Widow and surviving child of deceased united states citizen In the case of the death of a citizen of the United States, the Attorney General may exercise discretion described in clause (i) with respect to an alien who was a child of such citizen, or was the spouse of such citizen and was not legally separated from such citizen on the date of the citizen\u2019s death, if\u2014 (aa) the Attorney General determines that removal of the child or spouse or the denial of a requested benefit would result in hardship to the child or spouse; and (bb) the child or spouse seeks relief requiring such discretion not later than two years after the date of the citizen\u2019s death or demonstrates to the satisfaction of the Attorney General the existence of extraordinary circumstances that prevented the spouse or child from seeking relief within such period. (iii) Exclusions This subparagraph shall not apply to an alien whom the Attorney General determines\u2014 (I) is inadmissible under\u2014 (aa) paragraph (2) or (3) of section 212(a); or (bb) subparagraph (A), (C), or (D) of section 212(a)(10); or (II) is deportable under paragraph (2), (4), or (6) of section 237(a). .\n##### (b) Secretary\u2019s discretion\nSection 212 of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended\u2014\n**(1)**\nby redesignating the second subsection (t) as subsection (u); and\n**(2)**\nby adding at the end the following:\n(v) Secretary\u2019s discretion (1) In general In the case of an alien who is the spouse or child of a citizen of the United States, the Secretary of Homeland Security may, subject to paragraph (2)\u2014 (A) waive the application of one or more grounds of inadmissibility or deportability in connection with an application for an immigration benefit or request for relief from removal; (B) decline to issue a notice to appear or other charging document requiring such an alien to appear for removal proceedings; (C) decline to reinstate an order of removal under section 241(a)(5); or (D) grant such alien permission to reapply for admission to the United States or any other application for an immigration benefit. (2) Limitation on discretion (A) In general The Secretary of Homeland Security may exercise discretion described in paragraph (1) if the Secretary determines that removal of the alien or the denial of a requested benefit would result in hardship to the alien\u2019s United States citizen spouse, parent, or child. There shall be a presumption that family separation constitutes hardship. (B) Widow and orphan of deceased united states citizen In the case of the death of a citizen of the United States, the Secretary of Homeland Security may exercise discretion described in paragraph (1) with respect to an alien who was a child of such citizen, or was the spouse of such citizen and was not legally separated from such citizen on the date of the citizen\u2019s death, if\u2014 (i) the Secretary determines that the denial of a requested benefit would result in hardship to the child or spouse; and (ii) the child or spouse seeks relief requiring such discretion not later than two years after the date of the citizen\u2019s death or demonstrates to the satisfaction of the Secretary the existence of extraordinary circumstances that prevented the spouse or child from seeking relief within such period. (3) Exclusions This subsection shall not apply to an alien whom the Secretary determines\u2014 (A) is inadmissible under\u2014 (i) paragraph (2) or (3) of subsections (a); or (ii) subparagraphs (A), (C), or (D) of subsection (a)(10); or (B) is deportable under paragraphs (2), (4), or (6) of section 237(a). .\n#### 4. Motions to reopen or reconsider\n##### (a) In general\nA motion to reopen or reconsider the denial of a petition or application or an order of removal for an alien may be granted if such petition, application, or order would have been adjudicated in favor of the alien had this Act, or an amendment made by this Act, been in effect at the time of such denial or order.\n##### (b) Filing requirement\nA motion under subsection (a) shall be filed no later than the date that is 2 years after the date of the enactment of this Act, unless the alien demonstrates to the satisfaction of the Secretary of Homeland Security or Attorney General, as appropriate, the existence of extraordinary circumstances that prevented the alien from filing within such period.",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Homeland Security, Ways and Means, Transportation and Infrastructure, Education and Workforce, Oversight and Government Reform, and Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DIGNIDAD (Dignity) Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-04-04T16:57:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119hr2366",
          "measure-number": "2366",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-26",
          "originChamber": "HOUSE",
          "update-date": "2026-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2366v00",
            "update-date": "2026-01-17"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Families United Act</strong></p> <p>This bill authorizes the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to exercise discretion in certain immigration cases. </p> <p>Under this bill, DOJ or DHS may, on a case-by-case basis, exercise discretion by declining to remove a non-U.S. national (<i>alien</i> under federal law) or bar an alien from entering the United States to prevent hardship for the alien's U.S. citizen spouse, parent, or child. This discretion may also be exercised if the alien is the spouse or child of a deceased U.S. citizen.</p> <p>For the purposes of this bill, it shall be presumed that family separation constitutes hardship. </p> <p>However, DOJ or DHS may not exercise this discretion if the alien is removable or inadmissible due to certain grounds, including specified crime- and security-related grounds.</p> <p>This exercise of discretion may be applied to an alien who was ordered removed or denied entry prior to this bill's enactment if the alien files a motion to reopen or reconsider within two years of this bill's enactment.</p>"
        },
        "title": "American Families United Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2366.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Families United Act</strong></p> <p>This bill authorizes the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to exercise discretion in certain immigration cases. </p> <p>Under this bill, DOJ or DHS may, on a case-by-case basis, exercise discretion by declining to remove a non-U.S. national (<i>alien</i> under federal law) or bar an alien from entering the United States to prevent hardship for the alien's U.S. citizen spouse, parent, or child. This discretion may also be exercised if the alien is the spouse or child of a deceased U.S. citizen.</p> <p>For the purposes of this bill, it shall be presumed that family separation constitutes hardship. </p> <p>However, DOJ or DHS may not exercise this discretion if the alien is removable or inadmissible due to certain grounds, including specified crime- and security-related grounds.</p> <p>This exercise of discretion may be applied to an alien who was ordered removed or denied entry prior to this bill's enactment if the alien files a motion to reopen or reconsider within two years of this bill's enactment.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr2366"
    },
    "title": "American Families United Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Families United Act</strong></p> <p>This bill authorizes the Department of Homeland Security (DHS) or the Department of Justice (DOJ) to exercise discretion in certain immigration cases. </p> <p>Under this bill, DOJ or DHS may, on a case-by-case basis, exercise discretion by declining to remove a non-U.S. national (<i>alien</i> under federal law) or bar an alien from entering the United States to prevent hardship for the alien's U.S. citizen spouse, parent, or child. This discretion may also be exercised if the alien is the spouse or child of a deceased U.S. citizen.</p> <p>For the purposes of this bill, it shall be presumed that family separation constitutes hardship. </p> <p>However, DOJ or DHS may not exercise this discretion if the alien is removable or inadmissible due to certain grounds, including specified crime- and security-related grounds.</p> <p>This exercise of discretion may be applied to an alien who was ordered removed or denied entry prior to this bill's enactment if the alien files a motion to reopen or reconsider within two years of this bill's enactment.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr2366"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2366ih.xml"
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
      "title": "American Families United Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Families United Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to promote family unity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:47Z"
    }
  ]
}
```
