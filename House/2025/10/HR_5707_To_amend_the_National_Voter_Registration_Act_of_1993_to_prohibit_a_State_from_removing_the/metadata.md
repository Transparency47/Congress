# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5707
- Title: Voter Purge Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5707
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2026-04-08T13:06:24Z
- Update date including text: 2026-04-08T13:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5707",
    "number": "5707",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Voter Purge Protection Act",
    "type": "HR",
    "updateDate": "2026-04-08T13:06:24Z",
    "updateDateIncludingText": "2026-04-08T13:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T19:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "OH"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-08",
      "state": "DC"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "LA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NV"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
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
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MS"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TN"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "GA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CT"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CO"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "AL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "DE"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CO"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MI"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5707ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5707\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mrs. Beatty (for herself, Ms. Brown , Ms. Schakowsky , Ms. Norton , Mr. Fields , Mr. Jackson of Illinois , Ms. Titus , Mr. Huffman , Mr. Goldman of New York , Mr. Thompson of Mississippi , Mr. Cohen , Ms. Lois Frankel of Florida , Mr. Mullin , Mr. Bishop , Mr. Johnson of Georgia , Mr. Larson of Connecticut , Mrs. McIver , Mr. Veasey , Mr. Kennedy of New York , Ms. DeGette , Ms. Sewell , and Mr. Carson ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the National Voter Registration Act of 1993 to prohibit a State from removing the name of any registrant from the official list of voters eligible to vote in elections for Federal office in the State unless the State verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in such elections.\n#### 1. Short title\nThis Act may be cited as the Voter Purge Protection Act .\n#### 2. Conditions for removal of voters from list of registered voters\n##### (a) Conditions described\nThe National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ) is amended by inserting after section 8 the following new section:\n8A. Conditions for removal of voters from official list of registered voters (a) Verification on basis of objective and reliable evidence of ineligibility (1) Requiring verification Notwithstanding any other provision of this Act, a State may not remove the name of any registrant from the official list of voters eligible to vote in elections for Federal office in the State unless the State verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in such elections. (2) Factors not considered as objective and reliable evidence of ineligibility For purposes of paragraph (1), the following factors, or any combination thereof, shall not be treated as objective and reliable evidence of a registrant\u2019s ineligibility to vote: (A) The failure of the registrant to vote in any election. (B) The failure of the registrant to respond to any notice sent under section 8(d), unless the notice has been returned as undeliverable. (C) The failure of the registrant to take any other action with respect to voting in any election or with respect to the registrant\u2019s status as a registrant. (b) Notice after removal (1) Notice to individual removed (A) In general Not later than 48 hours after a State removes the name of a registrant from the official list of eligible voters for any reason, the State shall send notice of the removal to the former registrant, and shall include in the notice the grounds for the removal and information on how the former registrant may contest the removal or be reinstated, including a telephone number for the appropriate election official. (B) Exceptions Subparagraph (A) does not apply in the case of a registrant\u2014 (i) who sends written confirmation to the State that the registrant is no longer eligible to vote in the registrar\u2019s jurisdiction in which the registrant was registered; or (ii) who is removed from the official list of eligible voters by reason of the death of the registrant. (2) Public notice Not later than 48 hours after conducting any general program to remove the names of ineligible voters from the official list of eligible voters (as described in section 8(a)(4)), the State shall disseminate a public notice through such methods as may be reasonable to reach the general public (including by publishing the notice in a newspaper of wide circulation or posting the notice on the websites of the appropriate election officials) that list maintenance is taking place and that registrants should check their registration status to ensure no errors or mistakes have been made. The State shall ensure that the public notice disseminated under this paragraph is in a format that is reasonably convenient and accessible to voters with disabilities, including voters who have low vision or are blind. .\n##### (b) Conditions for transmission of notices of removal\nSection 8(d) of such Act ( 52 U.S.C. 20507(d) ) is amended by adding at the end the following new paragraph:\n(4) A State may not transmit a notice to a registrant under this subsection unless the State obtains objective and reliable evidence (in accordance with the standards for such evidence which are described in section 8A(a)(2)) that the registrant has changed residence to a place outside the registrar\u2019s jurisdiction in which the registrant is registered. .\n##### (c) Conforming amendments\n**(1) National Voter Registration Act of 1993**\nSection 8(a) of such Act ( 52 U.S.C. 20507(a) ) is amended\u2014\n**(A)**\nin paragraph (3), by striking provide and inserting subject to section 8A, provide ; and\n**(B)**\nin paragraph (4), by striking conduct and inserting subject to section 8A, conduct .\n**(2) Help America Vote Act of 2002**\nSection 303(a)(4)(A) of the Help America Vote Act of 2002 ( 52 U.S.C. 21083(a)(4)(A) ) is amended by striking , registrants and inserting , and subject to section 8A of such Act, registrants .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act.",
      "versionDate": "2025-10-08",
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
        "actionDate": "2025-10-09",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "2994",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Voter Purge Protection Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-05T22:05:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-08",
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
          "measure-id": "id119hr5707",
          "measure-number": "5707",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5707v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Voter Purge Protection Act </strong></p><p>This bill prohibits a state from removing registrants from the official list of eligible voters unless it meets certain verification and notice requirements.</p><p>Specifically, the bill prohibits a state from removing a registrant from the official list of eligible voters unless it verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in federal elections. Further, a state is prohibited from considering failure to vote in an election or failure to respond to a notice as evidence of ineligibility to vote.</p><p>Additionally, the bill requires a state to provide individual registrants who are removed with a notice, which must include the grounds for the removal and information on contesting the removal. Public notice must be provided after conducting any general program to remove the names of ineligible voters.</p>"
        },
        "title": "Voter Purge Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5707.xml",
    "summary": {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Voter Purge Protection Act </strong></p><p>This bill prohibits a state from removing registrants from the official list of eligible voters unless it meets certain verification and notice requirements.</p><p>Specifically, the bill prohibits a state from removing a registrant from the official list of eligible voters unless it verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in federal elections. Further, a state is prohibited from considering failure to vote in an election or failure to respond to a notice as evidence of ineligibility to vote.</p><p>Additionally, the bill requires a state to provide individual registrants who are removed with a notice, which must include the grounds for the removal and information on contesting the removal. Public notice must be provided after conducting any general program to remove the names of ineligible voters.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5707"
    },
    "title": "Voter Purge Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Voter Purge Protection Act </strong></p><p>This bill prohibits a state from removing registrants from the official list of eligible voters unless it meets certain verification and notice requirements.</p><p>Specifically, the bill prohibits a state from removing a registrant from the official list of eligible voters unless it verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in federal elections. Further, a state is prohibited from considering failure to vote in an election or failure to respond to a notice as evidence of ineligibility to vote.</p><p>Additionally, the bill requires a state to provide individual registrants who are removed with a notice, which must include the grounds for the removal and information on contesting the removal. Public notice must be provided after conducting any general program to remove the names of ineligible voters.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5707"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5707ih.xml"
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
      "title": "Voter Purge Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T09:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Voter Purge Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Voter Registration Act of 1993 to prohibit a State from removing the name of any registrant from the official list of voters eligible to vote in elections for Federal office in the State unless the State verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in such elections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T09:48:18Z"
    }
  ]
}
```
