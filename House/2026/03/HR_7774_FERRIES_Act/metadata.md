# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7774
- Title: FERRIES Act
- Congress: 119
- Bill type: HR
- Bill number: 7774
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-05-13T08:06:33Z
- Update date including text: 2026-05-13T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-03 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-03 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7774",
    "number": "7774",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000621",
        "district": "6",
        "firstName": "Emily",
        "fullName": "Rep. Randall, Emily [D-WA-6]",
        "lastName": "Randall",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "FERRIES Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:33Z",
    "updateDateIncludingText": "2026-05-13T08:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-03T17:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AK"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "WA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "WA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "WA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "DE"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7774ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7774\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Ms. Randall (for herself, Mr. Begich , Mr. Garamendi , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 23 and 49, United States Code, to codify and amend certain grant programs under which the Secretary of Transportation may issue grants for use in the provision of passenger ferry services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Enhancement and Revitalization of Reliable Infrastructure for Essential Seaways Act or the FERRIES Act .\nI\nAuthorizations\n#### 2. Funding for passenger ferry services grant programs\n##### (a) Construction of ferry boats and ferry terminal facilities\nSection 147(h) of title 23, United States Code, is amended by striking paragraphs (1) through (5) and inserting the following:\n(1) $160,000,000 for fiscal year 2027; (2) $162,000,000 for fiscal year 2028; (3) $164,000,000 for fiscal year 2029; (4) $166,000,000 for fiscal year 2030; and (5) $168,000,000 for fiscal year 2031. .\n##### (b) Urban passenger ferry grant program\n**(1) In general**\nSection 5307(h) of title 49, United States Code, is amended by adding at the end the following new paragraph:\n(4) Authorization of appropriations In addition to funds made available under section 5338 to carry out this section, there is authorized to be appropriated to the Secretary to carry out this subsection $200,000,000 for each of fiscal years 2027 through 2031. .\n**(2) Apportionments**\nSection 5336(h)(1) of title 49, United States Code, is amended by striking $30,000,000 and inserting $100,000,000 .\n##### (c) Ferry fleet modernization and shipyard job creation grant program\n**(1) Amendments to IIJA electric or low-emitting ferry pilot program**\nSection 71102 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 147 note) is amended\u2014\n**(A)**\nby striking the section heading and inserting Ferry fleet modernization and shipyard job creation grant program ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nby striking paragraph (3);\n**(ii)**\nby redesignating paragraph (2) as paragraph (3); and\n**(iii)**\nby inserting after paragraph (1) the following new paragraph:\n(2) Covered entity The term covered entity means a recipient or designated recipient eligible for a grant under section 5307 or 5311. ;\n**(C)**\nin subsection (b)\u2014\n**(i)**\nby striking a pilot program to provide grants and inserting a grant program under which the Secretary may issues grants to a covered entity ;\n**(ii)**\nby striking of or and inserting of, or ; and\n**(iii)**\nby striking from existing and inserting from, existing ;\n**(D)**\nin subsection (c)\u2014\n**(i)**\nby striking pilot program and inserting grant program ;\n**(ii)**\nby striking ensure that and inserting ensure that, to the extent practicable ;\n**(iii)**\nin paragraph (1), by striking shall ; and\n**(iv)**\nin paragraph (2), by striking shall ; and\n**(E)**\nin subsection (d) by striking $50,000,000 and all that follows through the period at the end and inserting $140,000,000 for each of fiscal years 2027 through 2031. .\n**(2) Codification**\nSection 71102 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 147 note), as amended, is transferred to appear as section 5313 of title 49, United States Code.\n**(3) Clerical amendment**\nThe analysis for chapter 53 of title 49, United States Code, is amended by inserting after the item relating to section 5312 the following:\n5313. Ferry fleet modernization and shipyard job creation grant program. .\n##### (d) Rural ferry grant program\n**(1) Amendments to IIJA ferry service grants**\nSection 71103 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 147 note) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (2)(B)\u2014\n**(I)**\nby striking the period at the end and inserting ; or ;\n**(II)**\nby striking served not and inserting the following:\nserved\u2014 (i) not ; and\n**(III)**\nby adding at the end the following:\n(ii) not less than 2 rural areas without regard to the distance between such areas. ; and\n**(ii)**\nby striking paragraph (4);\n**(B)**\nin subsection (b) by striking establish a program to and all that follows through the period at the end and inserting maintain a program under which the Secretary may provide competitive grants to States for the provision of a basic essential ferry service in rural areas. ;\n**(C)**\nin subsection (e) by striking under section 5336 or 5337 of title 49, United States Code, and inserting under section 5336 (other than subsection (h)(1) of such section) or 5337 ;\n**(D)**\nin subsection (f)\u2014\n**(i)**\nby striking the subsection heading and inserting Authorization of appropriations ; and\n**(ii)**\nby striking $200,000,000 and all that follows through the period at the end and inserting $300,000,000 for each fiscal years 2027 through 2031, of which $100,000,000 shall be derived from the Highway Trust Fund (other than the Mass Transit Account). ;\n**(E)**\nby redesignating subsections (f) and (g) as subsections (g) and (h), respectively; and\n**(F)**\nby inserting after subsection (e) the following:\n(f) Proportion of funds In carrying out the program under this section, the Secretary shall ensure that not less than 80 percent of the funds made available to eligible services under this section are provided to eligible services described in subsection (a)(2)(B)(i). .\n**(2) Codification**\n**(A) In general**\nChapter 53 of title 49, United States Code, is amended by inserting after section 5307 the following new section:\n5308. Ferry service for rural communities program .\n**(B) Transfer**\nSubsections (a) through (f) of section 71103 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 147 note), as amended by paragraph (1), are transferred to appear as subsections (a) through (f) of section 5308 of title 49, United States Code, as inserted by this paragraph.\n**(C) Clerical amendment**\nThe analysis for chapter 53 of title 49, United States Code, is amended by inserting after the item relating to section 5307 the following:\n5308. Ferry service for rural communities program. .\nII\nAppropriations\nThat the following sums are appropriated, out of any money in the Treasury not otherwise appropriated, and for other purposes, namely:\nDepartment of Transportation\nFederal Highway Administration\nhighway infrastructure programs\nFor an additional amount for Highway Infrastructure Programs , $500,000,000, to remain available until expended, to carry out the construction of ferry boats and ferry terminal facilities program under section 147 of title 23, United States Code: Provided , That $100,000,000, to remain available until expended, shall be made available for fiscal year 2027, $100,000,000, to remain available until expended, shall be made available for fiscal year 2028, $100,000,000, to remain available until expended, shall be made available for fiscal year 2029, $100,000,000, to remain available until expended, shall be made available for fiscal year 2030, and $100,000,000, to remain available until expended, shall be made available for fiscal year 2031: Provided further , That amounts made available under this heading in this Act shall be administered as if made available under section 147 of title 23, United States Code: Provided further , That the amounts made available under this heading in this Act shall be derived from the general fund of the Treasury, shall be in addition to any other amounts made available for such purpose, and shall not affect the distribution or amount of funds provided in any Act making annual appropriations: Provided further , That up to 1.5 percent of the amounts made available under this heading in this Act in each of fiscal years 2027 through 2031 shall be for operations and administrations of the Federal Highway Administration: Provided further , That the amounts made available under this heading in this Act shall not be subject to any limitation on obligations for Federal-aid highways or highway safety construction programs set forth in any Act making annual appropriations.\nFederal Transit Administration\ntransit infrastructure grants\nFor an additional amount for Transit Infrastructure Grants , $1,250,000,000, to remain available until expended, to carry out the passenger ferry grants program under section 5307(h) of title 49, United States Code: Provided , That $250,000,000, to remain available until expended, shall be made available for fiscal year 2027, $250,000,000, to remain available until expended, shall be made available for fiscal year 2028, $250,000,000, to remain available until expended, shall be made available for fiscal year 2029, $250,000,000, to remain available until expended, shall be made available for fiscal year 2030, and $250,000,000, to remain available until expended, shall be made available for fiscal year 2031: Provided further , That the amounts made available under this heading in this Act shall be derived from the general fund of the Treasury, shall be in addition to any other amounts made available for such purpose, and shall not affect the distribution of funds provided in any Act making annual appropriations: Provided further , That the amounts made available under this heading in this Act shall not be subject to any limitation on obligations for the Federal Public Transportation Assistance Program set forth in any Act making annual appropriations: Provided further , That not more than two percent of the amounts made available under this heading in this Act shall be available for administrative and oversight expenses as authorized under section 5334 and section 5338(c) of title 49, United States Code, and shall be in addition to any other appropriations for such purpose.\nferry service for rural communities program\nFor competitive grants to States for eligible essential ferry service as authorized under section 5308 of title 49, United States Code, $1,250,000,000, to remain available until expended: Provided , That $250,000,000, to remain available until expended, shall be made available for fiscal year 2027, $250,000,000, to remain available until expended, shall be made available for fiscal year 2028, $250,000,000, to remain available until expended, shall be made available for fiscal year 2029, $250,000,000, to remain available until expended, shall be made available for fiscal year 2030, and $250,000,000, to remain available until expended, shall be made available for fiscal year 2031: Provided further , That amounts made available under this heading in this Act shall be derived from the general fund of the Treasury: Provided further , That amounts made available under this heading in this Act shall not be subject to any limitation on obligations for the Federal Public Transportation Assistance Program set forth in any Act making annual appropriations: Provided further , That not more than two percent of the amounts made available under this heading in this Act shall be available for administrative and oversight expenses as authorized under section 5334 and section 5338(c) of title 49, United States Code, and shall be in addition to any other appropriations for such purpose.\nferry fleet modernization and shipyard job creation grant program\nFor competitive grants for the Ferry Fleet Modernization and Shipyard Job Creation Grant Program as authorized under section 5313 of title 49, United States Code, $500,000,000, to remain available until expended: Provided , That $100,000,000, to remain available until expended, shall be made available for fiscal year 2027, $100,000,000, to remain available until expended, shall be made available for fiscal year 2028, $100,000,000, to remain available until expended, shall be made available for fiscal year 2029, $100,000,000, to remain available until expended, shall be made available for fiscal year 2030, and $100,000,000, to remain available until expended, shall be made available for fiscal year 2031: Provided further , That amounts made available under this heading in this Act shall be derived from the general fund of the Treasury: Provided further , That the amounts made available under this heading in this Act shall not be subject to any limitation on obligations for transit programs set forth in any Act making annual appropriations: Provided further , That not more than two percent of the amounts made available under this heading in this Act shall be available for administrative and oversight expenses as authorized under section 5334 and section 5338(c) of title 49, United States Code, and shall be in addition to any other appropriations for such purpose.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-04-01T19:07:16Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7774ih.xml"
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
      "title": "FERRIES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FERRIES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Enhancement and Revitalization of Reliable Infrastructure for Essential Seaways Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 23 and 49, United States Code, to codify and amend certain grant programs under which the Secretary of Transportation may issue grants for use in the provision of passenger ferry services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:26Z"
    }
  ]
}
```
