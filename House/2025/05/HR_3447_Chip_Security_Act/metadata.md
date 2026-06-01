# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3447?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3447
- Title: Chip Security Act
- Congress: 119
- Bill type: HR
- Bill number: 3447
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-22T08:08:13Z
- Update date including text: 2026-05-22T08:08:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 0.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3447",
    "number": "3447",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Chip Security Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:13Z",
    "updateDateIncludingText": "2026-05-22T08:08:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
            "date": "2026-03-26T16:12:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T14:00:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
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
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
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
      "sponsorshipDate": "2025-05-15",
      "state": "AR"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
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
      "sponsorshipDate": "2025-05-15",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MD"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
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
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "IN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TN"
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
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "HI"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TN"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-07",
      "state": "OH"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "KY"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3447ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3447\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Huizenga (for himself, Mr. Foster , Mr. Moolenaar , Mr. Krishnamoorthi , Mr. Crawford , Mr. Lieu , Mr. LaHood , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of Commerce to issue standards with respect to chip security mechanisms for integrated circuit products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chip Security Act .\n#### 2. Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\ntechnology developed in the United States should serve as the foundation for the global ecosystem of artificial intelligence to advance the foreign policy and national security objectives of the United States and allies and partners of the United States;\n**(2)**\nthe United States can foster goodwill, strengthen relationships, and support innovative research around the world by providing allies and partners of the United States with advanced computing capabilities;\n**(3)**\nadvanced integrated circuits and computing hardware that is exported from the United States must be protected from diversion, theft, and other unauthorized use or exploitation in order to bolster the competitiveness of the United States and protect the national security of the United States;\n**(4)**\nimplementing chip security mechanisms will improve compliance with the export control laws of the United States, assist allies and partners with guarding computing hardware, and enhance protections from bad actors looking to access, divert, or tamper with advanced integrated circuits and computing hardware; and\n**(5)**\nimplementing chip security mechanisms may help with the detection of smuggling or exploitation of advanced integrated circuits and computing hardware, thereby allowing for increased flexibility in export controls and opening the door for more international partners to receive streamlined and larger shipments of advanced computing hardware.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(2) Chip security mechanism**\nThe term chip security mechanism means a software-, firmware-, or hardware-enabled security mechanism or a physical security mechanism.\n**(3) Covered integrated circuit product**\nThe term covered integrated circuit product means\u2014\n**(A)**\nan integrated circuit classified under Export Control Classification Number 3A090 or 3A001.z;\n**(B)**\na computer or other product classified under Export Control Classification Number 4A090 or 4A003.z; or\n**(C)**\nan integrated circuit or computer or a product containing an integrated circuit or computer that is classified under an Export Control Classification Number that is a successor or substantially similar to the numbers listed in subparagraphs (A) and (B).\n**(4) Export**\nThe term export has the meaning given that term in section 1742(3) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(3) ).\n**(5) In-country transfer**\nThe term in-country transfer has the meaning given that term in section 1742(6) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(6) ).\n**(6) Reexport**\nThe term reexport has the meaning given that term in section 1742(9) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(9) ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 4. Requirements for security mechanisms for export of integrated circuit products\n##### (a) Primary requirements for chip security mechanisms\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall require any covered integrated circuit product to be outfitted with chip security mechanisms that implement location verification, using techniques that are feasible and appropriate on such date of enactment, before it is exported, reexported, or in-country transferred to or in a foreign country.\n**(2) Notification requirement**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall require any person that has received a license or other authorization under the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) to export, reexport, or in-country transfer a covered integrated circuit product to promptly report to the Under Secretary of Industry and Security, if the person obtains credible information that the product\u2014\n**(A)**\nis in a location other than the location specified in the application for the license or other authorization;\n**(B)**\nhas been diverted to a user other than the user specified in the application; or\n**(C)**\nhas been subjected to tampering or an attempt at tampering, including efforts to disable, spoof, manipulate, mislead or circumvent location verification mechanisms or other chip security mechanisms.\n##### (b) Development of secondary requirements for chip security mechanisms\n**(1) Assessment**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary shall\u2014\n**(i)**\nconduct an assessment to identify what additional mechanisms, if any, should be added to the primary chip security mechanisms required under subsection (a)(1)\u2014\n**(I)**\nto enhance compliance with the requirements of the Export Control Reform Act of 2018;\n**(II)**\nto prevent, hinder, and detect the unauthorized use, access, or exploitation of covered integrated circuit products;\n**(III)**\nto identify and monitor smuggling intermediaries; and\n**(IV)**\nto achieve any national security or foreign policy objective of the United States that the Secretary considers appropriate; and\n**(ii)**\nif the Secretary identifies any such mechanism, develop requirements for outfitting covered integrated circuit products with that mechanism.\n**(B) Elements**\nThe assessment required by paragraph (1) shall include\u2014\n**(i)**\nan examination of the feasibility, reliability, and effectiveness of\u2014\n**(I)**\nmethods and strategies that prevent the tampering, disabling, or other manipulating of covered integrated circuit products;\n**(II)**\nworkload verification methods;\n**(III)**\nmethods to modify the functionality of covered integrated circuit products that have been illicitly acquired; and\n**(IV)**\nany other method the Secretary determines appropriate for the prevention of unauthorized use, access, or exploitation of covered integrated circuit products;\n**(ii)**\nan analysis of\u2014\n**(I)**\nthe potential costs associated with implementing each method examined under clause (i), including an analysis of\u2014\n**(aa)**\nthe potential impact of the method on the performance of covered integrated circuit products; and\n**(bb)**\nthe potential for the introduction of new vulnerabilities into the products;\n**(II)**\nthe potential benefits of implementing the methods examined under clause (i), including an analysis of the potential increase\u2014\n**(aa)**\nin compliance of covered integrated circuit products with the requirements of the Export Control Reform Act of 2018; and\n**(bb)**\nin detecting, hindering, and preventing unauthorized use, access, or exploitation of the products; and\n**(III)**\nthe susceptibility of the methods examined under clause (i) to tampering, disabling, or other forms of manipulation; and\n**(iii)**\nan estimate of the expected costs to implement at-scale methods to tamper with, disable, or manipulate a covered integrated circuit product, or otherwise circumvent the methods examined under clause (i).\n**(2) Report to congress**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report on the results of the assessment required by paragraph (1), including\u2014\n**(i)**\nan identification of the chip security mechanisms, if any, to be included in the requirements for secondary chip security mechanisms; and\n**(ii)**\nif applicable, a roadmap for the timely implementation of the secondary chip security mechanisms.\n**(B) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n**(3) Implementation**\n**(A) In general**\nIf any mechanisms are determined by the Secretary to be appropriate, the Secretary shall, not later than 2 years after the date on which the Secretary completes the assessment required by paragraph (1), require any covered integrated circuit product to be outfitted with the secondary chip security mechanisms identified pursuant to paragraph (1)(A) before the product is exported, reexported, or in-country transferred to or in a foreign country.\n**(B) Privacy**\nIn implementing requirements for secondary chip security mechanisms under subparagraph (A), the Secretary shall prioritize confidentiality.\n##### (c) Enforcement authority\nIn carrying out this section, the Secretary may\u2014\n**(1)**\nverify, in a manner the Secretary determines appropriate, the ownership and location of a covered integrated circuit product that has been exported, reexported, or in-country transferred to or in a foreign country;\n**(2)**\nmaintain a record of covered integrated circuit products and include in the record the location and current end-user of each such product; and\n**(3)**\nrequire any person who has been granted a license or other authorization under the Export Control Reform Act of 2018 to export, reexport, or in-country transfer a covered integrated circuit product to provide the information needed to maintain the record.\n##### (d) Annual assessment and report on new chip security mechanisms\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter for 3 years, the Secretary shall\u2014\n**(1)**\nconduct an assessment of new chip security mechanisms that have been developed in the year preceding the date of the assessment; and\n**(2)**\nsubmit to the appropriate congressional committees a report that includes\u2014\n**(A)**\na summary of the results of the assessment required by paragraph (1);\n**(B)**\nan evaluation of whether any of the new mechanisms assessed under paragraph (1) should be added to or replace any of the existing requirements for secondary chip security mechanisms developed under subsection (b)(1); and\n**(C)**\nany recommendations for modifications to relevant export controls to allow for more flexibility with respect to the countries to or in which covered integrated circuit products may be exported, reexported, or in-country transferred if the products include chip security mechanisms that meet the requirements developed under subsection (b)(1).",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-08",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1705",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chip Security Act",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-04-06T20:26:30Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-06T20:26:43Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T20:26:37Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-06T20:26:33Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-04-06T20:26:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-23T17:41:38Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3447ih.xml"
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
      "title": "Chip Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chip Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Commerce to issue standards with respect to chip security mechanisms for integrated circuit products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:25Z"
    }
  ]
}
```
