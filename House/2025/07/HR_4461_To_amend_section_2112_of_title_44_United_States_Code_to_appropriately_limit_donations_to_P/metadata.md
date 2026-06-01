# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4461?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4461
- Title: To amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.
- Congress: 119
- Bill type: HR
- Bill number: 4461
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-12-05T22:56:21Z
- Update date including text: 2025-12-05T22:56:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4461",
    "number": "4461",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "To amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.",
    "type": "HR",
    "updateDate": "2025-12-05T22:56:21Z",
    "updateDateIncludingText": "2025-12-05T22:56:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NM"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MD"
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
      "sponsorshipDate": "2025-07-16",
      "state": "DC"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IN"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
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
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MO"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NV"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "PA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sponsorshipDate": "2025-08-15",
      "state": "HI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "RI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MN"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4461ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4461\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Moskowitz (for himself, Ms. Stansbury , Mr. Raskin , Ms. Norton , Mr. Carson , Ms. Williams of Georgia , Mr. Johnson of Georgia , Mrs. Watson Coleman , Mr. Min , Mr. Cleaver , Mr. Evans of Pennsylvania , Mr. Pallone , Ms. Titus , Ms. Clarke of New York , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.\n#### 1. Requirements for Presidential Libraries and Centers\nSection 2112 of title 44, United States Code, is amended by adding at the end the following:\n(h) Requirements for Presidential Libraries and Centers (1) Definitions In this subsection\u2014 (A) the term donation \u2014 (i) includes\u2014 (I) any gift, subscription, loan, advance, or deposit of money or anything of value made by any person directly or indirectly to a Presidential Library or Center, including donations to the United States Government or another entity for subsequent delivery to the Presidential Library or Center; and (II) the payment by any person of compensation or the provision of anything of value for the personal services of another person, for any purpose, which are rendered to the Presidential Library or Center without charging the Presidential Library or Center; and (ii) does not include the value of services provided without compensation by any individual who volunteers on behalf of the Presidential Library or Center; (B) the term Federal contractor has the meaning given that term under section 115.1 of title 11, Code of Federal Regulations, or any successor thereto; (C) the term foreign national has the meaning given that term under section 319(b) of the Federal Election Campaign Act of 1971; (D) the term 501(c)(3) tax exempt organization means an organization which is described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code; (E) the term Presidential Library or Center means an organization established to raise funds to create, maintain, expand, or conduct activities at\u2014 (i) a Presidential archival depository; (ii) any facility relating to a Presidential archival depository; or (iii) any private museum, foundation, center, or other facility that is\u2014 (I) affiliated with an individual who is serving or served in the office of President; (II) established on or after the date on which the first campaign of the individual for the office of President commenced; and (III) designed to commemorate the legacy of the individual as a President; (F) the term registered agent of a foreign principal means a person who is registered or is required to be registered as an agent of a foreign principal (as defined in section 1 of the Foreign Agents Registration Act of 1938 ( 22 U.S.C. 611 )) under that Act; and (G) the term registered lobbyist means a lobbyist, as defined in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ), that is registered or required to register under section 4(a) of that Act ( 2 U.S.C. 1603(a) ). (2) Restrictions (A) Restrictions on source of donations It shall be unlawful for a Presidential Library or Center, an officer or employee thereof, or the Archivist to solicit, accept, receive, or agree to accept or receive in the future a donation from a person if, on the date on which the donation is solicited, accepted, received, or agreed to be accepted or received in the future\u2014 (i) the individual for whom the Presidential Library or Center is or will be established is serving in or has been elected to the office of President; and (ii) the person from whom the donation is solicited, accepted, received, or agreed to be accepted or received in the future\u2014 (I) is not registered as a 501(c)(3) tax exempt organization; or (II) is\u2014 (aa) a registered lobbyist; (bb) a registered agent of a foreign principal; (cc) a Federal contractor; (dd) a foreign national; or (ee) seeking or has received a pardon from the President for whom the Presidential Library or Center is established. (B) Restrictions on persons making donations It shall be unlawful for a person to directly or indirectly make a donation, or make an express or implied promise to make a donation, directly or indirectly, to a Presidential Library or Center if, on the date on which the donation or promise is made\u2014 (i) the individual for whom the Presidential Library or Center is or will be established is serving in or has been elected to the office of President; and (ii) the person making the donation or promise\u2014 (I) is not registered as a 501(c)(3) tax exempt organization; or (II) is\u2014 (aa) a registered lobbyist; (bb) a registered agent of a foreign principal; (cc) a Federal contractor; (dd) a foreign national; or (ee) seeking or has received a pardon from the President for whom the Presidential Library or Center is established. (C) Cooling off period for certain donations (i) Restrictions on acceptance of certain donations During the 2-year period following the date on which the individual for whom a Presidential Library or Center is established ceases to serve in the office of the President, it shall be unlawful for the Presidential Library or Center, an officer or employee thereof, or the Archivist to solicit, accept, receive, or agree to accept or receive in the future a donation from a person who, on the date on which the donation is solicited, accepted, received, or agreed to be accepted or received in the future\u2014 (I) is a registered lobbyist; (II) is a registered agent of a foreign principal; (III) is a Federal contractor; (IV) is a foreign national; or (V) is seeking or has received a pardon from the President for whom the Presidential Library or Center is established. (ii) Restrictions on persons making donations During the 2-year period following the date on which the individual for whom a Presidential Library or Center is established ceases to serve in the office of the President, it shall be unlawful for a person to directly or indirectly make a donation, or make an express or implied promise to make a donation, to a Presidential Library or Center if, on the date on which the donation or promise is made, the person making the donation or promise\u2014 (I) is a registered lobbyist; (II) is a registered agent of a foreign principal; (III) is a Federal contractor; (IV) is a foreign national; or (V) is seeking or has received a pardon from the President for whom the Presidential Library or Center is established. (D) Conversion of donation to personal use It shall be unlawful for any person, at any time, to convert a donation to a Presidential Library or Center to the personal use of any person, which shall include a circumstance in which any part of the donation is used to fulfill a commitment, obligation, or expense of a person that would exist irrespective of the responsibilities of the Presidential Library or Center. (3) Aggregate donation limit (A) In general It shall be unlawful for any person to make donations to a Presidential Library or Center the value of which, in the aggregate, exceeds $10,000 during the period\u2014 (i) beginning on the date on which the individual for whom the Presidential Library or Center is established has been elected to the office of President; and (ii) ending on the date that is 1 year after the date on which such individual ceases serving in the office of President. (B) Indexing for inflation (i) In general At the beginning of the first year during which presidential and vice-presidential electors are chosen after the date of enactment of this subsection, and the beginning of each such year thereafter, the amount described in subparagraph (A) shall be increased by the cumulative percent difference determined under section 315(c)(1)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30116(c)(1)(A) ) since the most recent prior year during which such electors were chosen. (ii) Rounding The amount of an increase under clause (i) shall be rounded to the nearest multiple of $1,000. (4) Reporting requirements (A) Definitions In this paragraph\u2014 (i) the term covered period means the period\u2014 (I) beginning\u2014 (aa) on the date on which the individual has been elected to the office of President; or (bb) with respect to the individual serving as President on the date of enactment of this subsection, on the date of enactment of this subsection; and (II) ending on the date that is 5 years the date on which the individual ceases serving in the office of President; and (ii) the term covered person means a person who made 1 or more donations to the applicable Presidential Library or Center during the applicable calendar quarter in an aggregate amount that is not less than $200. (B) Reporting Not later than 15 days after the end of each calendar quarter occurring during the covered period with respect to an individual who serves as President, a Presidential Library or Center established for such individual shall file with the Archivist a report disclosing any donation during the calendar quarter made by a covered person. (C) Contents A report filed under subparagraph (B) for a calendar quarter shall contain, for each donation of money or anything of value made to the Presidential Library or Center by a covered person during the quarter\u2014 (i) the amount or value of the donation; (ii) the date the donation is received; (iii) the name, address, and employer of the individual making the donation; and (iv) if the source of the donation is an individual, the occupation of the individual. (D) Use of another\u2019s name for donation During the covered period with respect to an individual who serves as President, it shall be unlawful for a person to knowingly\u2014 (i) make a donation to a Presidential Library or Center established for such individual in the name of another person; (ii) permit the name of that person to be used to effect a donation by another person to a Presidential Library or Center established for such individual; (iii) accept a donation to a Presidential Library or Center established for such individual made by one person in the name of another person; or (iv) direct, help, or assist any person in making a contribution in the name of another person. (E) Publication Not later than 30 days after the date on which each report is filed under subparagraph (B), the Archivist shall publish the complete report on the website of the National Archives and Records Administration, which shall be available without a fee or other access charge, and in a searchable, sortable, and downloadable format. (5) Enforcement (A) In general The Attorney General may bring a civil or criminal action, and the attorney general of any State may bring a civil action, seeking relief for a violation of this subsection in an appropriate district court of the United States. (B) General penalty (i) Civil Any person who violates this subsection shall be subject to\u2014 (I) a civil penalty that does not exceed the greater of $20,000 or the amount equal to the aggregate value of the donations involved in such violation; and (II) an order requiring the person to disgorge any donation involved in the violation. (ii) Criminal Any person who knowingly and willfully violates this section shall be\u2014 (I) fined under title 18, imprisoned for not more than 1 year, or both; and (II) subject to an order requiring the person to disgorge any donation involved in the violation. (C) Increased penalty for large donations (i) Civil Any person who violates this subsection, if the violation of this subsection involves the soliciting, accepting, making, receiving, agreeing to accept or receive, promising to make, conversion, effecting, or reporting of 1 or more donations during a calendar year with an aggregate value of more than $50,000, shall be subject to\u2014 (I) a civil penalty that does not exceed the greater of $100,000 or the amount equal to the aggregate value of the donations involved in such violation; and (II) an order requiring the person to disgorge any donation involved in the violation. (ii) Criminal Any person who knowingly and willfully violates this subsection, if the violation of this subsection involves the soliciting, accepting, making, receiving, agreeing to accept or receive, promising to make, conversion, effecting, or reporting of 1 or more donations during a calendar year with an aggregate value of more than $50,000, shall be\u2014 (I) fined under title 18, imprisoned for not more than 5 years, or both; and (II) subject to an order requiring the person to disgorge any donation involved in the violation. (D) Types of relief A court may grant a permanent or temporary injunction, restraining order, or other order, upon a proper showing that the person involved has committed, or is about to commit a violation of this section. (E) Period of limitations (i) Civil A civil action under this subsection may not be commenced later than 10 years after the cause of action accrues. (ii) Criminal No person shall be prosecuted, tried, or punished for any offense under this subsection, unless the indictment is found or the information is instituted within 10 years after such offense shall have been committed. (F) Indexing for inflation (i) In general At the beginning of the first year during which presidential and vice-presidential electors are chosen after the date of enactment of this subsection, and the beginning of each such year thereafter, the amounts described in subparagraphs (B) and (C) shall be increased by the cumulative percent difference determined under section 315(c)(1)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30116(c)(1)(A) ) since the most recent prior year during which such electors were chosen. (ii) Rounding The amount of an increase under clause (i) shall be rounded to the nearest multiple of $1,000. (6) Regulations The Archivist shall promulgate regulations, which shall be published in the Federal Register, for the purpose of carrying out this subsection. .",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-07-16",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2300",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.",
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
        "updateDate": "2025-08-01T16:14:17Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4461ih.xml"
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
      "title": "To amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:18Z"
    },
    {
      "title": "To amend section 2112 of title 44, United States Code, to appropriately limit donations to Presidential Libraries and Centers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:57Z"
    }
  ]
}
```
