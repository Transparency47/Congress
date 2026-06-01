# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2994
- Title: Voter Purge Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2994
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2026-01-09T12:03:23Z
- Update date including text: 2026-01-09T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2994",
    "number": "2994",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Voter Purge Protection Act",
    "type": "S",
    "updateDate": "2026-01-09T12:03:23Z",
    "updateDateIncludingText": "2026-01-09T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
        "item": [
          {
            "date": "2025-10-09T16:23:22Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-09T16:23:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MN"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-09",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-10-09",
      "state": "ME"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "VA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MD"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "PA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NJ"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "MI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
      "state": "DE"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "DE"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2994is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2994\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Padilla (for himself, Ms. Klobuchar , Mr. Murphy , Mr. Van Hollen , Ms. Smith , Mr. Sanders , Mrs. Gillibrand , Mr. King , Mr. Kaine , Mr. Schiff , Ms. Alsobrooks , Ms. Hirono , Mrs. Shaheen , Mr. Blumenthal , Ms. Warren , Mr. Booker , Mr. Merkley , Ms. Duckworth , Mr. Fetterman , Mr. Wyden , Mr. Markey , Mr. Kim , Mr. Peters , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the National Voter Registration Act of 1993 to clarify that a State may not use an individual\u2019s failure to vote as the basis for initiating the procedures provided under such Act for the removal of the individual from the official list of registered voters in the State on the grounds that the individual has changed residence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Voter Purge Protection Act .\n#### 2. Purpose\nThe purposes of this Act are\u2014\n**(1)**\nto prohibit States from removing individuals from an official list of registered voters due to changes in residence; and\n**(2)**\nto protect the right to vote by allowing voters who are automatically registered or had previously registered to vote in a State to update their address through the day of the election.\n#### 3. Conditions for removal of voters from list of registered voters\n##### (a) Conditions described\nThe National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ) is amended by inserting after section 8 the following new section:\n8A. Conditions for removal of voters from official list of registered voters (a) Verification on basis of objective and reliable evidence of ineligibility (1) Requiring verification Notwithstanding any other provision of this Act, a State may not remove the name of any registrant from the official list of voters eligible to vote in elections for Federal office in the State unless the State verifies, on the basis of objective and reliable evidence, that the registrant is ineligible to vote in such elections. (2) Factors not considered as objective and reliable evidence of ineligibility For purposes of paragraph (1), except as permitted under section 8(d) after a notice described in paragraph (2) of such section has been sent, the following factors, or any combination thereof, shall not be treated as objective and reliable evidence of a registrant\u2019s ineligibility to vote: (A) The failure of the registrant to vote in any election. (B) The failure of the registrant to respond to any election mail, unless the election mail has been returned as undeliverable. (C) The failure of the registrant to take any other action with respect to voting in any election or with respect to the registrant\u2019s status as a registrant. (3) Removal based on official records (A) In general Nothing in this section shall prohibit a State from removing a registrant from the official list of eligible voters in elections for Federal office if, on the basis of official records maintained by the State, a State or local election official knows, on the basis of objective and reliable evidence, that the registrant has\u2014 (i) died; or (ii) permanently moved out of the State and is no longer eligible to vote in the State. (B) Opportunity to demonstrate eligibility The State shall provide a voter removed from the official list of eligible voters in elections for Federal office under this paragraph an opportunity to demonstrate that the registrant is eligible to vote and be reinstated on the official list of eligible voters in elections for Federal office in the State. (b) Notice after removal (1) Notice to individual removed (A) In general Not later than 48 hours after a State removes the name of a registrant from the official list of eligible voters, the State shall send notice of the removal to the former registrant, and shall include in the notice the grounds for the removal and information on how the former registrant may contest the removal or be reinstated, including a telephone number for the appropriate election official. (B) Exceptions Subparagraph (A) does not apply in the case of a registrant\u2014 (i) who sends written confirmation to the State that the registrant is no longer eligible to vote in the registrar\u2019s jurisdiction in which the registrant was registered; or (ii) who is removed from the official list of eligible voters by reason of the death of the registrant. (2) Public notice Not later than 48 hours after conducting any general program to remove the names of ineligible voters from the official list of eligible voters (as described in section 8(a)(4)), the State shall disseminate a public notice through such methods as may be reasonable to reach the general public (including by publishing the notice in a newspaper of wide circulation and posting the notice on the websites of the appropriate election officials) that list maintenance is taking place and that registrants should check their registration status to ensure no errors or mistakes have been made. The State shall ensure that the public notice disseminated under this paragraph is in a format that is reasonably convenient and accessible to voters with disabilities, including voters who have low vision or are blind. .\n##### (b) Conditions for transmission of notices of removal\nSection 8(d) of such Act ( 52 U.S.C. 20507(d) ) is amended by adding at the end the following new paragraph:\n(4) A State may not transmit a notice to a registrant under this subsection unless the State obtains objective and reliable evidence (in accordance with the standards for such evidence which are described in section 8A(a)(2)) that the registrant has changed residence to a place outside the registrar\u2019s jurisdiction in which the registrant is registered. .\n##### (c) Conforming amendments\n**(1) National Voter Registration Act of 1993**\nSection 8(a) of such Act ( 52 U.S.C. 20507(a) ) is amended\u2014\n**(A)**\nin paragraph (3), by striking provide and inserting subject to section 8A, provide ; and\n**(B)**\nin paragraph (4), by striking conduct and inserting subject to section 8A, conduct .\n**(2) Help America Vote Act of 2002**\nSection 303(a)(4)(A) of the Help America Vote Act of 2002 ( 52 U.S.C. 21083(a)(4)(A) ) is amended by striking registrants the second place it appears and inserting and subject to section 8A of such Act, registrants .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act.\n#### 4. State registration portability\n##### (a) In general\nSection 8(e) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507(e) ) is amended to read as follows:\n(e) Procedure for voting following failure To return card Notwithstanding failure to notify the registrar of the change of address prior to the date of an election, a registrant who has moved from an address in the State to an address in the same State shall, upon oral or written affirmation by the registrant of the change of address before an election official, be permitted to vote (at the option of the voter)\u2014 (1) at the polling place of the registrant\u2019s current address; or (2) at a central location within the same registrar\u2019s jurisdiction. .\n##### (b) Effective date\nThe amendment made by this section shall take effect on the date of the enactment of this Act.",
      "versionDate": "2025-10-09",
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
        "actionDate": "2025-10-08",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "5707",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Voter Purge Protection Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-05T22:05:45Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2994is.xml"
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
      "title": "Voter Purge Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Voter Purge Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Voter Registration Act of 1993 to clarify that a State may not use an individual's failure to vote as the basis for initiating the procedures provided under such Act for the removal of the individual from the official list of registered voters in the State on the grounds that the individual has changed residence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:15Z"
    }
  ]
}
```
