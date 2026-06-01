# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6875
- Title: AI OVERWATCH Act
- Congress: 119
- Bill type: HR
- Bill number: 6875
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-21T08:07:51Z
- Update date including text: 2026-05-21T08:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6875",
    "number": "6875",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "AI OVERWATCH Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:51Z",
    "updateDateIncludingText": "2026-05-21T08:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:09:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AR"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "OH"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NJ"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "GU"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "OH"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "AS"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "SC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IA"
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
      "sponsorshipDate": "2026-03-04",
      "state": "OH"
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
      "sponsorshipDate": "2026-03-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "RI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "MN"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NE"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6875ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6875\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Mast (for himself, Mr. Huizenga , Mr. Moolenaar , Mrs. Kim , Mr. Self , Mr. Crawford , and Mr. LaHood ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Under Secretary of Commerce for Industry and Security to require a license for the export, reexport, or in-country transfer of certain integrated circuits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act or the AI OVERWATCH Act .\n#### 2. License requirement for exports of covered integrated circuits to countries of concern\nPart I of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) is amended by inserting after section 1758 the following:\n1758A. Control of exports of covered integrated circuits (a) Definitions In this section: (1) Appropriate congressional committees the term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate. (2) Commerce control list The term Commerce Control List means the list set forth in Supplement No. 1 to part 774 of the Export Administration Regulations. (3) Country of concern The term country of concern means\u2014 (A) the People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions; (B) the Republic of Cuba; (C) the Islamic Republic of Iran; (D) the Democratic People\u2019s Republic of Korea; (E) the Russian Federation; and (F) the Bolivarian Republic of Venezuela under the regime of Nicol\u00e1s Maduro Moros. (4) Covered integrated circuit (A) In general Subject to subparagraphs (B), (C), and (D), the term covered integrated circuit means\u2014 (i) an integrated circuit, computer, or other product\u2014 (I) classified under Export Control Classification Number 3A090 or 4A090 or related Export Control Classification Numbers; or (II) that is functionally equivalent or substantially similar to a circuit, computer, or product described in subclause (I), including certain similar products listed under Export Control Classification Number 5A002.z; or (ii) an integrated circuit that has 1 or more digital processing units with\u2014 (I) a total processing performance of 4,800 or more; (II) a total processing performance of 2,400 or more and a performance density of 1.6 or more; (III) a total processing performance of 1,600 or more and a performance density of 3.2 or more; or (IV) a total DRAM bandwidth of 1,400 gigabytes per second or more, interconnect bandwidth of 1,100 gigabytes per second or more, or a sum of DRAM bandwidth and interconnect bandwidth of 1,700 gigabytes per second or more. (B) Authority to update technical parameters Beginning 18 months after the date of the submission to Congress of the national security strategy required in subsection (g), the Under Secretary may add or modify technical parameters for the definition of covered integrated circuit for purposes of this section, if the Operating Committee for Export Policy has approved the new or modified technical parameters by majority vote. (C) Products included Except as provided by subparagraph (D), the term covered integrated circuit includes a product containing such a covered integrated circuit. (D) Exclusion The term covered integrated circuit does not include a covered integrated circuit or a product containing such a covered integrated circuit that is not designed or marketed for use in data centers. (5) Operating Committee for Export Policy The term Operating Committee for Export Policy means the Operating Committee for Export Policy referred to in section 1763(c) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( 50 U.S.C. 4822(c) ). (6) Performance density; total processing performance The terms performance density and total processing performance have the meanings given those terms in, and are calculated as provided for under, Export Control Classification Number 3A090 in the Commerce Control List (as in effect on December 15, 2025). (7) Trusted United States person The term trusted United States person means any United States person designated as a trusted United States person pursuant to subsection (d)(2). (b) License requirement (1) In general Beginning on the date of the enactment of this section, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall require a license for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern. (2) General license prohibited The Under Secretary may not issue a general license for the purpose of fulfilling the license requirement in paragraph (1). (c) Certification to Congress (1) Certification requirement Not fewer than 30 days prior to approving any license for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall submit to the appropriate congressional committees a copy of the license application, including\u2014 (A) the quantity of covered integrated circuit, identified by an Export Control Classification Number, as applicable, and by technical parameters of the covered integrated circuit; (B) the ultimate consignee or end-user of the covered integrated circuit; (C) any and all license conditions; (D) a certification that the export, reexport, or in-country transfer of the covered integrated circuit has verifiable and enforceable mechanisms for ensuring the ultimate consignee or end-user has not, does not, and will not support or enable, directly or indirectly, the military, intelligence, surveillance, or cyber-enabled capabilities of a country of concern, including\u2014 (i) an explanation of how the license conditions support the certification; and (ii) in the case that the license concerns a country of concern that engages in a military-civil fusion policy or maintains a law that requires persons to provide support and assistance to national security bodies, public security bodies, or relevant military bodies of the country of concern, details on how the license conditions address the specific threats arising from such policy or law; (E) a certification that approving the license will not adversely impact the availability of covered integrated circuits for United States persons, including a certification that all of the major subcomponents of the covered integrated circuits, such as high-bandwidth memory, are available in sufficient supply to fulfill the entirety of the demand of United States persons; and (F) a certification that approving the license will not adversely impact the advantage of the United States in total nationally-installed processing power capacity relative to the country of concern related to the ultimate consignee or end user of the covered integrated circuit; (G) the underlying analyses supporting the certifications required in subparagraphs (D), (E), and (F); and (H) a technical assessment (including an alternative assessment by the Director of National Intelligence, if applicable) of how the export, re-export, or in-country transfer of the covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern affects the artificial intelligence leadership of the United States, including in terms of global market share, in artificial intelligence models, artificial intelligence cloud services, and covered integrated circuits, respectively. (2) Limitation (A) In general The license described in subsection (b) may not be issued\u2014 (i) until the date that is not fewer than 30 days after the committees described paragraph (1) received the certification required in such paragraph; and (ii) if Congress, prior to the date that is 30 days after such committees received such certification, enacts a joint resolution prohibiting the proposed export, reexport, or in-country transfer. (B) Joint resolution (i) Consideration in the Senate Any joint resolution under this subsection shall be considered in the Senate in accordance with the provisions of section 601(b) of the International Security Assistance and Arms Export Control Act of 1976 ( Public Law 94\u2013329 ; 90 Stat. 765). (ii) Consideration in the House of Representatives For the purpose of expediting the consideration and enactment of joint resolutions under this subsection, a motion to proceed to the consideration of any such joint resolution after it has been reported by the appropriate committee shall be treated as highly privileged in the House of Representatives. (d) Exemption from certain license requirements for trusted United States persons (1) In general The requirement for a license under sections 742.6 and 744.23 of the Export Administration Regulations shall not apply to the export, reexport, or in-country transfer of a covered integrated circuit if the covered integrated circuit\u2014 (A) is destined for a country that is not a country of concern; and (B) remains under the ownership and control of a trusted United States person or the subsidiaries of a trusted United States person once the covered integrated circuit is in operation. (2) Implementation Not later than 90 days after the date of the enactment of this section, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is part of the Operating Committee for Export Policy, shall\u2014 (A) seek input from the public regarding the standards and requirements a United States person should be required to meet to obtain a designation as a trusted United States person; (B) based on such input, prescribe regulations establishing such standards and requirements, which shall include\u2014 (i) establishment by the United States person of reasonable security standards, including physical security, cybersecurity, remote access, secure covered integrated circuit repair and disposal procedures, and other measures designed to prevent the illicit transfer, diversion, or access to covered integrated circuits; (ii) a requirement that the United States person may not transfer or install a majority of its aggregate total processing performance of covered integrated circuits outside the United States; (iii) a requirement that not more than 10 percent of the ultimate beneficial ownership of the United States person may be held, directly or indirectly, by any entity that primarily resides, is domiciled, or conducts the majority of its business in a country of concern; (iv) a preference for sourcing advanced integrated circuits and subcomponents from production facilities that support the revival of semiconductor manufacturing in the United States; and (v) annual audit or attestation requirements to ensure compliance with clauses (i), (ii), and (iii); and (C) prescribe regulations establishing the process by which the Under Secretary, in coordination with each agency that is part of the Operating Committee for Export Policy, shall approve such a designation. (3) Allied expansion The Under Secretary, in coordination with each agency that is part of the Operating Committee for Export Policy, shall consider options for securely expanding the license exemption program described in this subsection to allies of the United States. (e) Termination of licenses Any license issued or approved prior to the date of the enactment of this section for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern is terminated. (f) Temporary prohibition The Under Secretary, in coordination with each agency that is part of the Operating Committee for Export Policy, shall deny all licenses for the export, reexport, or in-country transfer of a covered integrated circuit to an entity that is located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern until the date that is 14 days after the submission to Congress of the national security strategy required in subsection (g). (g) National Security Strategy The Secretary of Commerce, in conjunction with the Secretary of State, the Secretary of Defense, the Secretary of Energy, the United States Trade Representative, the Secretary of the Treasury, and the Director of the White House Office of Science and Technology Policy, and in consultation with the Director of National Intelligence, shall submit to the appropriate congressional committees a strategy that details\u2014 (1) the national security implications of and goals that should govern the physical and remote access by countries of concern to covered integrated circuits, semiconductor manufacturing equipment, and related subcomponents that are from the United States or allies of the United States; (2) an assessment of the implications of the export, re-export, or in-country transfer of covered integrated circuits to countries of concern for the military, intelligence, surveillance, or cyber-enabled capabilities of such countries; and (3) an assessment by the Director of National Intelligence of the covered integrated circuit production numbers and capabilities of the People\u2019s Republic of China for fiscal year 2026, including\u2014 (A) a determination of whether the Chinese Communist Party would cease or reduce its efforts to pursue indigenous production and use of Chinese-designed and manufactured covered integrated circuits if entities located or headquartered in, or the ultimate parent company of which is headquartered in, the People\u2019s Republic of China are provided access to covered integrated circuits designed in the United States; (B) a comparison of the covered integrated circuit production numbers and capabilities of the People\u2019s Republic of China to the covered integrated circuit production numbers and capabilities of the United States and allies of the United States; and (C) a quantitative analysis examining the artificial intelligence capabilities of countries of concern if such countries relied solely on indigenous production of covered integrated circuits using indigenously produced manufacturing equipment and related subcomponents. .",
      "versionDate": "2025-12-18",
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
        "name": "International Affairs",
        "updateDate": "2025-12-19T20:32:49Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6875ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Under Secretary of Commerce for Industry and Security to require a license for the export, reexport, or in-country transfer of certain integrated circuits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:56Z"
    },
    {
      "title": "AI OVERWATCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI OVERWATCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Artificial Intelligence Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:18Z"
    }
  ]
}
```
