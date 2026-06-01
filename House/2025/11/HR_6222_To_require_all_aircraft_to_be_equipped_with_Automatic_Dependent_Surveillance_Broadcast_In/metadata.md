# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6222
- Title: ROTOR Act
- Congress: 119
- Bill type: HR
- Bill number: 6222
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-16T15:28:41Z
- Update date including text: 2026-05-16T15:28:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Sponsor introductory remarks on measure. (CR H4853)
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Sponsor introductory remarks on measure. (CR H4853)
- 2025-11-21 - Committee: Referred to the Subcommittee on Aviation.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6222",
    "number": "6222",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert F. [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "ROTOR Act",
    "type": "HR",
    "updateDate": "2026-05-16T15:28:41Z",
    "updateDateIncludingText": "2026-05-16T15:28:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4853)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:26:12Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "RI"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "OR"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "GA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "OH"
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
      "sponsorshipDate": "2026-02-13",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "DE"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
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
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-20",
      "state": "MA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "HI"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MN"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "OH"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "WA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "RI"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6222ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6222\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Onder (for himself and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require all aircraft to be equipped with Automatic Dependent Surveillance-Broadcast In, to improve aviation safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rotorcraft Operations Transparency and Oversight Reform Act or the ROTOR Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) ADS-B In**\nThe term ADS-B In means onboard avionics equipment that receives and processes Automatic Dependent Surveillance-Broadcast transmissions that are broadcast in accordance with sections 91.225 and 91.227 of title 14, Code of Federal Regulations (or any successor regulations), and other aviation advisory information from ground stations, that provides the aircraft with awareness to the location of other aircraft and traffic advisories.\n**(3) ADS-B Out**\nThe term ADS-B Out \u2014\n**(A)**\nhas the meaning given such term in section 91.227 of title 14, Code of Federal Regulations; and\n**(B)**\nbroadcasts information from the aircraft in accordance with sections 91.225 and 91.227 of such title 14 (or any successor regulations).\n**(4) Affected aircraft**\nThe term affected aircraft means any aircraft that is required to operate in accordance with section 91.225 of title 14, Code of Federal Regulations, or any successor regulation.\n**(5) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives.\n**(6) Cabinet member**\nThe term Cabinet Member means an individual who is the head (including an acting head) of the Department of Agriculture, the Department of Commerce, the Department of Defense, the Department of Education, the Department of Energy, the Department of Health and Human Services, the Department of Homeland Security, the Department of Housing and Urban Development, the Department of the Interior, the Department of Justice, the Department of Labor, the Department of State, the Department of Transportation, the Department of the Treasury, or the Department of Veterans Affairs, or any other individual who occupies a position designated by the President as a Cabinet-level position.\n**(7) FAA**\nThe term FAA means the Federal Aviation Administration.\n**(8) National Capital Region; NCR**\nThe terms National Capital Region and NCR mean the geographic area located within the boundaries of\u2014\n**(A)**\nthe District of Columbia;\n**(B)**\nMontgomery and Prince Georges Counties in the State of Maryland;\n**(C)**\nArlington, Fairfax, Loudoun, and Prince William Counties and the City of Alexandria in the Commonwealth of Virginia; and\n**(D)**\nall cities and other units of government within the geographic areas described in subparagraphs (A) through (C).\n**(9) Powered-lift**\nThe term powered-lift \u2014\n**(A)**\nhas the meaning given such term in section 1.1 of title 14, Code of Federal Regulations (or any successor regulation); and\n**(B)**\nincludes vertical-lift flight mode and wing-borne flight mode, as such terms are defined in section 194.103 of title 14, Code of Federal Regulations (or any successor regulation).\n**(10) Rotorcraft**\nThe term rotorcraft has the meaning given such term in section 1.1 of title 14, Code of Federal Regulations (or any successor regulation).\n**(11) Transport airplane**\nThe term transport airplane has the meaning given such term in section 44741(i) of title 49, United States Code.\n**(12) Unmanned aircraft system**\nThe term unmanned aircraft system has the meaning given such term in section 44801 of title 49, United States Code.\n#### 3. Revision to Exception for ADS-B Out Transmission\n##### (a) ADS-B Out reforms\n**(1) In general**\nBeginning on the date of enactment of this section, in applying section 91.225(f)(1) of title 14, Code of Federal Regulations, the term sensitive government mission shall be narrowly construed and shall not include training flights, proficiency flights, or flights of Federal officials below the rank of Cabinet Member.\n**(2) Rulemaking and administrative action**\n**(A) In general**\nNot later than 1 year after the date of enactment of this section, the Administrator shall\u2014\n**(i)**\nissue or revise regulations to update section 91.225(f) of title 14, Code of Federal Regulations, to comply with the requirements of this section; and\n**(ii)**\nrevise any memorandum of agreement between the FAA and any other Federal, State, local, or Tribal agency to conform with the revised regulations described in clause (i).\n**(B) Report**\nIf the Administrator fails to issue or revise regulations pursuant to subparagraph (A) or revise any memorandum of agreement between the FAA and any other agency pursuant to such subparagraph, the Administrator shall, within 30 days, submit to the appropriate committees of Congress a report on the status of such regulations, including the reasons that the Administrator has failed to issue or revise such regulations within the period required under such subparagraph.\n##### (b) GAO review and report\nNot later than the date that is 2 years after the date of enactment of this section, the Comptroller General of the United States shall\u2014\n**(1)**\nreview the utilization of exceptions under section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a), to determine\u2014\n**(A)**\nwhether the Department of Defense and other relevant Federal agencies or other applicable operators have utilized such exceptions in accordance with relevant laws and regulations; and\n**(B)**\nthe extent of such utilization;\n**(2)**\ncompare the utilization of exceptions specified in such section 91.225(f) before and after the issuance of revised regulations under subsection (a); and\n**(3)**\nsubmit to the Administrator and the appropriate committees of Congress a report on the findings of the review conducted under paragraph (1) and the comparison conducted under paragraph (2).\n##### (c) FAA review of non-Compliant operators\nUpon submission of the report under subsection (b)(3), the Administrator shall\u2014\n**(1)**\ndetermine whether any Federal agency or other applicable operator that has been found to have not utilized the exceptions under section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a), in accordance with relevant laws and regulations shall be permitted to continue to utilize such exceptions; and\n**(2)**\nnot later than 30 days after the date on which the Comptroller General submits the report under subsection (b)(3), brief the appropriate committees of Congress on such determination.\n##### (d) Reports\n**(1) To the Administrator**\nNot later than 90 days after the date of enactment of this section, and on a quarterly basis thereafter, each Federal, State, local, and Tribal agency that performs sensitive government missions as described in section 91.225(f)(1) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a), shall submit to the Administrator a report that includes\u2014\n**(A)**\nan attestation that such operations are regularly transmitting ADS-B Out and are conducted with proper consideration to aviation safety; and\n**(B)**\na list of operations delineated by flight in which the ADS-B Out equipment is not in transmit mode because the aircraft was performing a sensitive government mission, including the airport, airspace location, date, time, duration, and mission type of each such operation.\n**(2) To Congress**\n**(A) In general**\nNot later than 180 days after the date of enactment of this section, and biannually thereafter, the Administrator shall submit to the appropriate committees of Congress a report on the frequency and nature of the ADS\u2013B Out exceptions granted to Federal, State, local, and Tribal agencies under section 91.225(f)(1) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a). Such report\u2014\n**(i)**\nshall include\u2014\n**(I)**\naggregated data on the operations in which ADS-B Out equipment is not in transmit mode by each agency described in paragraph (1); and\n**(II)**\na determination from the Administrator as to whether each operation described in paragraph (1)(B) jeopardizes aviation safety; and\n**(ii)**\nmay include a classified annex.\n**(B) Special notification**\nIf an agency described in paragraph (1) operates a flight using an exception granted under section 91.225(f)(1) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a), 5 or more times in a calendar month, or fails to provide to the Administrator the attestation required under paragraph (1)(A), the Administrator shall notify the appropriate committees of Congress of such use within 14 days of being notified of such use. For the purposes of this subparagraph, a flight shall be interpreted as the period beginning when an aircraft moves under its own power for the purpose of flight and ending when the aircraft lands.\n##### (e) Annual Inspector General audits\n**(1) In general**\nBeginning on the date that is 3 years after the date of enactment of this section, the Inspector General of the Department of Transportation (in this section referred to as the Inspector General ) shall conduct an annual audit of FAA oversight of all operations that utilize an exception under section 91.225(f) of title 14, Code of Federal Regulations (or any successor regulation), as revised under subsection (a), including Federal agency operations.\n**(2) Considerations**\nIn conducting an audit under paragraph (1), the Inspector General shall assess the efficacy of FAA oversight related to the following:\n**(A)**\nEnsuring exceptions under such section 91.225(f)(1) (or any successor regulation) are strictly utilized by operators in accordance with relevant laws and regulations.\n**(B)**\nEnsuring exceptions under such section 91.225(f)(1) (or any successor regulation) are not routinely used by operators.\n**(C)**\nIdentifying and engaging with any operator not in compliance with relevant laws and regulations relating to exceptions under such section 91.225(f)(1) (or any successor regulation).\n**(D)**\nAny other factor determined appropriate by the Inspector General.\n**(3) Briefings to Congress**\nThe Inspector General shall brief the appropriate committees of Congress on an annual basis after the completion of each annual audit.\n#### 4. ADS\u2013B In requirements\n##### (a) Requirement for ADS-B In operation\n**(1) In general**\nNot later than 2 years after the date of enactment of this section, the Administrator shall issue a final rule in accordance with section 553 of title 5, United States Code, to require any person operating an aircraft (other than an unmanned aircraft, as defined in section 44801 of title 49, United States Code) required to be equipped with ADS\u2013B Out in accordance with section 91.225 of title 14, Code of Federal Regulations (or any successor regulation), to be equipped with and operating with ADS\u2013B In equipment that provides the aircraft with awareness to the location of other aircraft and traffic advisories, unless otherwise authorized by air traffic control.\n**(2) Compliance deadlines**\nIn issuing a final rule under paragraph (1), the Administrator shall\u2014\n**(A)**\ninclude an effective date of not later than 60 days after the date on which such final rule is published in the Federal Register; and\n**(B)**\nrequire aircraft described in paragraph (1) to be equipped with ADS-B In not later than December 31, 2031.\n**(3) Final regulation requirements**\nIn issuing a final rule under paragraph (1), the Administrator shall, at a minimum, do the following:\n**(A) Performance standards**\nThe Administrator shall establish appropriate performance requirements for ADS-B In equipment to provide integrated safety-enhancing capabilities for a pilot or other flight crew, including by increasing situational awareness to the location of other aircraft and providing traffic advisories with alerting sufficient to provide traffic advisory indications while airborne and on the airport surface, such as visual and aural advisories.\n**(B) Alternative equipment or technology**\nWith respect to aircraft with a maximum certificated takeoff weight of less than 12,500 pounds when operating under part 91 of title 14, Code of Federal Regulations, the Administrator shall establish performance requirements for alternative equipment or technology that the Administrator determines acceptable in satisfying the ADS-B In requirement. The performance requirements shall, at a minimum\u2014\n**(i)**\nprovide similar or improved situational awareness to the location of other airborne traffic, as well as traffic advisory information; and\n**(ii)**\nleverage the use of portable ADS-B In receivers or equipment that allow display on an existing or future electronic flight bag or panel mounted display, provided that the installation or use of such equipment does not adversely affect other required avionics or the airworthiness of the aircraft.\n**(C) Guidance**\nThe Administrator shall issue relevant guidance for aircraft operators and other appropriate stakeholders regarding the types of equipment that satisfy the performance requirements described in this paragraph.\n**(4) Other requirements**\nIn issuing a final rule under paragraph (1), the Administrator shall include\u2014\n**(A)**\nrequirements for ADS-B In equipment and the use of such equipment;\n**(B)**\ntechnical assistance to facilitating ADS-B In equipage across the entire fleet of affected aircraft, including, as appropriate, guidance under part 26 of title 14, Code of Federal Regulations, to provide support for affected transport airplane operators in complying with the requirements of this section;\n**(C)**\nany other associated guidance necessary to assist operators and other stakeholders in identifying equipment that satisfies the ADS-B In performance standards described in paragraph (3) prior to the compliance deadline described in paragraph (2)(B);\n**(D)**\na determination of alternative equipment or technology described in subsection (e); and\n**(E)**\na presumption, absent clear and compelling evidence to the contrary, that ADS-B In equipment is cost beneficial and improves aviation safety.\n**(5) Congressional briefings**\nNot later than 180 days after the date of enactment of this section, and every 90 days thereafter, the Administrator shall brief the appropriate committees of Congress, as well as publish a publicly available report, on the status of\u2014\n**(A)**\nthe ADS-B In rulemaking required under paragraph (1); and\n**(B)**\nafter the compliance deadline described in paragraph (2)(A), the implementation and oversight of such ADS-B In requirement.\n##### (b) Negotiated rulemaking committee\n**(1) Committee**\n**(A) In general**\nNot later than 60 days after the date of enactment of this section, the Administrator may establish a negotiated rulemaking committee (in this section referred to as the committee ) pursuant to section 565 of title 5, United States Code, to negotiate proposed regulations to implement the requirements described in subsection (a).\n**(B) Membership**\nIf the Administrator elects to establish a committee under this subsection, the committee shall be composed of\u2014\n**(i)**\nrepresentatives of\u2014\n**(I)**\nthe FAA;\n**(II)**\nair carriers;\n**(III)**\navionics manufacturers;\n**(IV)**\naircraft manufacturers; and\n**(V)**\ngeneral aviation organizations;\n**(ii)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7511 of title 5, United States Code;\n**(iii)**\norganizations representing certified collective bargaining representatives of airline pilots, including the principal organization representing the largest certified collective bargaining representative of airline pilots;\n**(iv)**\naviation safety experts outside of the FAA; and\n**(v)**\nany other representatives determined appropriate by the Administrator.\n**(2) Requirements**\nIf the Administrator elects to establish a committee under this subsection, the Administrator shall do the following:\n**(A) In general**\nThe Administrator shall direct the committee to make recommendations relating to\u2014\n**(i)**\nADS-B In equipment and its use;\n**(ii)**\nADS-B In equipment performance standards pursuant to subsection (a)(3);\n**(iii)**\nthe consideration of effective approaches to facilitating ADS-B In equipage across the entire fleet of affected aircraft, including requirements under part 26 of title 14, Code of Federal Regulations, to provide support for affected transport category airplane operators in complying with the requirements of this section; and\n**(iv)**\nwith respect to aircraft with a maximum certificated takeoff weight of less than 12,500 pounds when operating under part 91 of title 14, Code of Federal Regulations, a recommendation for low-cost alternative equipment or technology in accordance with subsection (e).\n**(B) Lack of committee consensus**\nIn the event the committee does not reach a consensus regarding a recommendation for low-cost alternative equipment or technology under subparagraph (A)(iv), the Administrator shall, after the submission of the committee under paragraph (3), consider prescribing a low-cost alternative that includes the criteria described in subsection (e).\n**(3) Submission to the Administrator**\nIf the Administrator elects to establish a committee under this subsection, not later than 1 year after the date of enactment of this section, the committee shall submit to the Administrator\u2014\n**(A)**\na consensus proposal of regulations to implement the requirement described in subsection (a)(1); or\n**(B)**\nin the event the committee does not reach a consensus, a report identifying any points of agreement and disagreement with respect to such proposed regulations.\n**(4) Proposed rule**\nIf the Administrator elects to establish a committee under this subsection, not later than 180 days after receiving the submission of the committee under paragraph (3), the Administrator shall issue a proposed rule, in accordance with section 553 of title 5, United States Code, that either\u2014\n**(A)**\nto the maximum extent possible consistent with the legal obligations of the FAA, uses the consensus proposal of the committee under paragraph (3)(A) as the basis for the proposed rule for notice and comment, including with respect to any standards or requirements described in subsection (a)(3); or\n**(B)**\nin the event the committee does not reach a consensus, considers the points of agreement and disagreement submitted by the committee under paragraph (3)(B).\n##### (c) Consultation required without negotiated rulemaking committee\nIf the Administrator does not establish a committee under subsection (b), prior to issuing a final rule, the Administrator shall consult with appropriate stakeholders in conducting the rulemaking required under subsection (a)(1), including at a minimum the representatives described in subsection (b)(1)(B).\n##### (d) Phased-In retrofit\n**(1) In general**\nIn issuing a final rule under subsection (a)(1), the Administrator shall\u2014\n**(A)**\nestablish a process by which the operator of an affected aircraft, in service as of the date on which the final rule under subsection (a)(1) is published in the Federal Register in accordance with subsection (a)(2)(A), may apply to the Administrator to request additional time, not to exceed a period of 1 year after the deadline described in subsection (a)(2)(B), to finalize equipage of its fleet and make ADS-B In operational, provided that\u2014\n**(i)**\nan aircraft operator, owner, or their agent submits an application deemed acceptable to the Administrator for additional time for compliance, including a justification for such request and an attestation of actions to date demonstrating progress toward achieving compliance;\n**(ii)**\nthe Administrator, in consultation with the Secretary of Transportation, determines additional time is required to mitigate a significant disruption to air transportation; and\n**(iii)**\nthe Administrator determines the aircraft operator or owner does not have any uncorrected violations of subchapters F and G of chapter I of title 14, Code of Federal Regulations; and\n**(B)**\nnotify the appropriate committees of Congress not later than 14 days after making a determination under clause (ii) or (iii) of subparagraph (A).\n**(2) Special rule for agents**\nWith the exception of an agent representing an owner or operator of transport airplanes, for the purposes of this subsection, an agent may represent more than 1 aircraft operator or owner of the same type, model, or manufacturer and may submit 1 or more applications under paragraph (1)(A)(i), each of which may contain multiple aircraft operators or owners.\n##### (e) Low-Cost alternative method of compliance\nIn issuing a final rule under subsection (a)(1), the Administrator shall determine low-cost equipment or technologies that provide similar or improved situational awareness to the location of other airborne traffic, as well as traffic advisory information, that satisfy the ADS-B In equipage requirement for aircraft with a maximum certificated takeoff weight of less than 12,500 pounds when operated under part 91 of title 14, Code of Federal Regulations. In making such a determination, the Administrator shall consider the use of\u2014\n**(1)**\nportable ADS-B In receivers; and\n**(2)**\nequipment that allows display on an existing or future electronic flight bag or panel mounted display, provided the installation or use does not adversely affect other required avionics or the airworthiness of the aircraft.\n##### (f) Proactive equipage\nWith respect to any aircraft for which ADS-B In equipment is available and complies with the requirements of the final rule issued under subsection (a)(1), the operator of any such aircraft shall take all appropriate actions necessary to equip such aircraft with ADS-B In prior to the compliance deadline described in subsection (a)(2).\n##### (g) Separation standards; relevant controller training\n**(1) Rulemaking**\n**(A) In general**\nNot later than 18 months after the effective date of the final rule described in subsection (a), the Administrator shall issue a notice of proposed rulemaking to establish separation standards, as appropriate, that leverage ADS-B Out or ADS-B In equipment, and all other available technological capabilities in the air traffic control system, to achieve safety and efficiency benefits throughout the national airspace system, including on an airport surface and within Class E airspace (as defined in section 71.71 of title 14, Code of Federal Regulations, or any successor regulation).\n**(B) Consultation**\nIn conducting the rulemaking under this subsection, the Administrator shall consult with appropriate stakeholders, including, at a minimum\u2014\n**(i)**\nrepresentatives of\u2014\n**(I)**\nair carriers;\n**(II)**\noriginal equipment manufacturers; and\n**(III)**\ngeneral aviation organizations;\n**(ii)**\norganizations representing certified collective bargaining representatives of airline pilots, including the principal organization representing the largest certified collective bargaining representative of airline pilots;\n**(iii)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7111 of title 5, United States Code;\n**(iv)**\naviation safety experts from outside the FAA; and\n**(v)**\nany other stakeholder deemed appropriate by the Administrator.\n**(2) Required updates to FAA Orders**\nNot later than 18 months after the issuance of the notice of proposed rulemaking under paragraph (1)(A), the Administrator shall complete revisions, as appropriate, to FAA Order 7110.65 and other relevant FAA Orders, to increase safety and efficiency benefits in the national airspace system.\n**(3) Relevant controller training**\n**(A) In general**\nNot later than 1 year after the compliance deadline described in subsection (a)(2), the Administrator shall revise initial and recurrent air traffic controller training, as appropriate, in accordance with FAA Orders 3000.22 and 3120.4 and revise associated orders and directives, as appropriate, to ensure such controllers are trained to apply any new separation standards and procedures.\n**(B) Requirements**\nIn revising training under subparagraph (A), the Administrator shall\u2014\n**(i)**\nconsider human factors impacts, appropriate phraseology adjustments, and surface movement applications; and\n**(ii)**\nconsult with the exclusive bargaining representative of air traffic controllers of the FAA certified under section 7111 of title 5, United States Code.\n##### (h) ACAS-X action plan\n**(1) In general**\nNot later than 180 days after the date of enactment of this section, the Administrator shall submit to the appropriate committees of Congress an action plan for advancing the deployment of the Airborne Collision Avoidance System-X (in this section referred to as ACAS-X ), or any variant or successor technology, in the national airspace system. The Administrator shall publish the action plan in a publicly available format not later than 10 days after submitting such action plan to Congress.\n**(2) Contents**\nIn developing the action plan under paragraph (1), the Administrator shall include\u2014\n**(A)**\na strategic roadmap for the deployment of ACAS-X technology, including steps required for widespread adoption among aircraft operators (including rotorcraft operators);\n**(B)**\nactions and funding necessary to complete any applicable research, development, testing, evaluation, and standards development needed to support the certification of such technology;\n**(C)**\nplans for engagement with appropriate stakeholders, including\u2014\n**(i)**\naircraft operators, including those in the Department of Defense;\n**(ii)**\naviation safety experts outside the FAA;\n**(iii)**\navionics manufacturers;\n**(iv)**\naircraft manufacturers;\n**(v)**\ngeneral aviation organizations;\n**(vi)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7511 of title 5, United States Code;\n**(vii)**\norganizations representing certified collective bargaining representatives of airline pilots, including the principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(viii)**\nany other stakeholders determined appropriate by the Administrator;\n**(D)**\nengagement with foreign civil aviation authorities to harmonize international standards for certification of such technology;\n**(E)**\nACAS-X interoperability considerations for aircraft operators (including rotorcraft operators) equipped with ADS-B Out and ADS-B In equipment;\n**(F)**\nan assessment of safety benefits for aircraft operators equipping with such technology, including civil and military operators; and\n**(G)**\nany recommendations for administrative or legislative action, as determined appropriate by the Administrator, to advance such technology deployment.\n**(3) Implementation**\nThe Administrator may take actions, as appropriate, to implement the action plan developed under paragraph (1).\n**(4) Briefing**\nNot later than 30 days after the date on which the Administrator submits the action plan under paragraph (1), the Administrator shall brief the appropriate committees of Congress on the contents of such action plan and any prospective actions to implement such plan.\n##### (i) ARAC tasking\n**(1) In general**\nThe Administrator shall task the Aviation Rulemaking Advisory Committee (in this section referred to as the ARAC ) with reviewing and assessing the need for aircraft operating in Class D airspace to be equipped with ADS-B Out and ADS-B In equipment.\n**(2) Report and recommendations**\nNot later than 1 year after initiating the review and assessment under this section, the ARAC shall submit to the Administrator\u2014\n**(A)**\na report on the findings of the review and assessment under paragraph (1); and\n**(B)**\nany recommendations for legislative or regulatory action the ARAC determines appropriate.\n**(3) Briefing**\nNot later than 30 days after the date on which the ARAC submits the report under paragraph (2), the Administrator shall brief the appropriate committees of Congress on\u2014\n**(A)**\nthe findings and recommendations included in such report; and\n**(B)**\nany plan to implement such recommendations, including a justification for any recommendations the Administrator determines should not be implemented.\n#### 5. Inspector General of the Army audit\n##### (a) In general\nNot later than 60 days after the date of enactment of this section, the Inspector General of the Army shall initiate an audit to evaluate the Army\u2019s coordination with the FAA, pilot training, and qualification standards, and the Army\u2019s use of ADS-B Out and whether it adheres to Army policy, regulation, and law.\n##### (b) Assessment\nIn conducting the audit required by subsection (a), the Inspector General of the Army shall assess practices and recommendations for the Army, including\u2014\n**(1)**\nwhether Army policy and United States law was adhered to, and the Army\u2019s coordination with the FAA, during National Capital Region ( NCR ) operations of pilot training and qualifications standards in the NCR;\n**(2)**\nthe Army\u2019s policy on ADS-B Out equipage, usage, and activation;\n**(3)**\nmaintenance protocols for UH\u201360 Black Hawk helicopters operated by the 12th Army Aviation Brigade including, but not limited to, the calibration of any system that transmits altitude and position information outside the aircraft and the calibration of systems that send altitude and position information to the pilots inside the aircraft, and the frequency with which such maintenance protocols occur;\n**(4)**\ncompliance with the September 29, 2021, Letter of Agreement executed between the Pentagon Heliport Air Traffic Control Tower and the Ronald Reagan Washington National Airport Air Traffic Control Tower regarding flight operations in the NCR; and\n**(5)**\nthe Army\u2019s review of loss of separation incidents involving its rotorcraft in the NCR along with possible mitigations to prevent future mishaps.\n##### (c) Public disclosure\nNot later than 14 days after the audit required by subsection (a) is concluded, the Secretary of the Army shall\u2014\n**(1)**\ntransmit a report on the results of the audit, without redactions, to the Committee on Commerce, Science, and Transportation and the Committee on Armed Services of the Senate and the Committee on Transportation and Infrastructure and the Committee on Armed Services of the House of Representatives; and\n**(2)**\npublicly release the report without redactions, except to the extent required for national security reasons.\n##### (d) Interim reporting\nNot later than 180 days after initiating the audit required by subsection (a), and every 180 days thereafter until such audit is concluded, the Inspector General of the Army shall brief the committees of Congress described in subsection (c)(1) regarding the progress of such audit.\n#### 6. Safety reviews of airspace\n##### (a) FAA-DOD coordination\nNot later than 30 days after the date of enactment of this section, the Administrator shall establish or designate an office within the FAA as the Office of FAA-DOD Coordination (in this section referred to as the Office ), which shall\u2014\n**(1)**\ncoordinate airspace usage of military aircraft and rotorcraft with relevant FAA lines of business, including the Air Traffic Organization;\n**(2)**\ncoordinate with the Office of Audit and Evaluation of the FAA to ensure employee complaints and whistleblower protections are considered;\n**(3)**\nconsider opportunities to improve management and consolidation of aviation safety information system databases to enhance civil and military aviation incident reporting; and\n**(4)**\ncarry out the safety review required by subsection (b).\n##### (b) Safety reviews\n**(1) Review of Ronald Reagan Washington National Airport**\n**(A) In general**\nNot later than 30 days after the date on which the Office is established or designated, the Administrator shall initiate a safety review of all military, law enforcement, and civilian rotary wing, powered lift, fixed wing, and unmanned aircraft system flight operations and flight routes in the Washington DC Metropolitan Area Special Flight Rules Area, including but not limited to flight operations conducted by the Department of Defense, emergency response providers, and air medical transport operators, to evaluate any associated safety risk to commercial transport airplane operations at Ronald Reagan Washington National Airport.\n**(B) Consultation**\nIn conducting a safety review under subparagraph (A), the Administrator shall consult with\u2014\n**(i)**\nthe Secretary of Defense;\n**(ii)**\nFederal, State, and local agencies;\n**(iii)**\nlaw enforcement agencies;\n**(iv)**\nemergency response providers, including air medical transport operators;\n**(v)**\nair carriers;\n**(vi)**\naviation labor organizations, including, at a minimum\u2014\n**(I)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7511 of title 5, United States Code; and\n**(II)**\norganizations representing certified collective bargaining representatives of airline pilots, including the principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(vii)**\nother stakeholders determined appropriate by the Administrator.\n**(2) Other airport reviews**\n**(A) In general**\nThe Administrator shall conduct safety reviews of all military, law enforcement and civilian rotary wing, powered lift, fixed wing, and unmanned aircraft system flight operations and flight routes at other Class B airports (as listed in section 1 of Appendix D to part 91 of title 14, Code of Federal Regulations (or any successor regulation)) and within the lateral boundary of Class B airspace, at commercial service Class C airports (as listed in FAA Order JO 7400.11J (or any successor order)) and within the lateral boundary of Class C airspace in the national airspace system, and at Class D airports that provide passenger service under part 121 of title 14, Code of Federal Regulations, determined to meet the risk criteria set forth in subparagraph (C), including flight operations conducted by the Department of Defense, emergency response providers, and air medical transport operators, to evaluate any associated safety risk to commercial transport airplane operations.\n**(B) Consultation**\nIn conducting a safety review under subparagraph (A), the Administrator shall consult with\u2014\n**(i)**\nthe Secretary of Defense;\n**(ii)**\nFederal, State, local, and Tribal agencies;\n**(iii)**\nlaw enforcement agencies;\n**(iv)**\nemergency response providers;\n**(v)**\nair carriers;\n**(vi)**\naviation labor organizations, including, at a minimum\u2014\n**(I)**\nthe exclusive bargaining representative of air traffic controllers of the FAA certified under section 7511 of title 5, United States Code; and\n**(II)**\norganizations representing certified collective bargaining representatives of airline pilots, including the principal organization representing the largest certified collective bargaining representative of airline pilots; and\n**(vii)**\nother stakeholders determined appropriate by the Administrator.\n**(C) Prioritization and risk criteria**\nIn prioritizing the safety reviews of Class B, Class C, and Class D airports described in subparagraph (A) and conducting the safety reviews pursuant to subparagraph (A), the Administrator shall, at a minimum, consider the following risk criteria:\n**(i)**\nThe type of airspace the airport is located in and the type of tower at the airport.\n**(ii)**\nWhether the airport has radar on the field.\n**(iii)**\nThe total number of air traffic operations at the airport per calendar year, as reported in the Operations Network (OPSNET) data of the FAA, and the rate of growth measured over a 20-year period prior to the initiation of a safety review under this section.\n**(iv)**\nThe Traffic Collision Avoidance System (TCAS) resolution advisory rates at the airport compared to the number of arrivals at the airport.\n**(v)**\nThe presence of parallel runways.\n**(vi)**\nThe presence of visual flights (in this subparagraph referred to as VFR ) corridors in proximity to the airport.\n**(vii)**\nThe presence of a helicopter corridor in proximity to the airport or nearby helicopter operations.\n**(viii)**\nThe presence of dense VFR operations at the airport.\n**(ix)**\nThe presence of complex VFR procedures at the airport or in the adjacent airspace.\n**(D) Deadline of initiation of reviews**\nThe Administrator shall initiate the reviews under this paragraph by the following deadlines:\n**(i) Class B airports**\nWith respect to Class B airports, not later than 90 days after the date of enactment of this section.\n**(ii) Class C airports**\nWith respect to Class C airports, not later than 90 days after the initiation date of the Class B airport reviews.\n**(iii) Class D airports**\nWith respect to Class D airports, not later than 90 days after the initiation date of the Class C airport reviews.\n**(3) Requirements**\nIn conducting the safety reviews required by paragraphs (1) and (2), the Office shall do the following:\n**(A)**\nAnalyze air traffic and airspace management.\n**(B)**\nEvaluate the level of coordination the Administrator exercises with the Secretary of Defense and the heads of any other Federal agencies, and emergency response providers as appropriate, to inform the designation and approval of airspace use and flight routes for non-transport airplane operations.\n**(C)**\nAssess any risks posed to transport airplanes from military aircraft and rotorcraft, civil rotorcraft, powered lift aircraft, and unmanned aircraft systems operating in Class B, Class C, or Class D airspace in proximity to Class B, Class C, or Class D airports.\n**(D)**\nReview relevant incidents submitted to the Administrator through Air Traffic Mandatory Occurrence reports (as documented via FAA Form 7210\u201313), Aviation Safety Reporting System reports, and Aviation Safety Action Program reports, and relevant reports submitted to the Administrator of the National Aeronautics and Space Administration through the Aviation Safety Reporting System, to identify any safety trends regarding the operation of military aircraft and rotorcraft, civil rotorcraft, powered lift aircraft, and unmanned aircraft systems in Class B, Class C, or Class D airspace near Class B, Class C, or Class D airports.\n**(4) Deadlines for completion of safety reviews**\n**(A) Ronald Reagan Washington National Airport**\nThe Administrator shall complete the safety review required by paragraph (1) not later than 120 days after the date on which such review is initiated.\n**(B) Other airports**\nThe Administrator shall complete a safety review required by paragraph (2) not later than 180 days after such review is initiated.\n**(5) Reports**\n**(A) Review of Ronald Reagan Washington National Airport**\nNot later than 60 days after completing the safety review required by paragraph (1), the Administrator shall submit to the appropriate committees of Congress a report detailing the analyses and results of such review, together with relevant findings and recommendations, including any corrective action plans to address any risks identified, and recommendations for legislative or administrative action determined appropriate by the Administrator.\n**(B) Other airport reviews**\nNot later than 6 months after the date of enactment of this section, and every 6 months thereafter, the Administrator shall submit to the appropriate committees of Congress a report detailing the analyses and results of the safety reviews completed pursuant to paragraph (2) since the preceding report under this subparagraph (or, in the case of the first such report, since such date of enactment), together with relevant findings and recommendations, including any corrective action plans to address any risks identified, and recommendations for legislative or administrative actions determined appropriate by the Administrator.\n**(6) Designation**\nThe Administrator shall designate a person within the Senior Executive Service of the FAA to be directly responsible for the completion of the requirements of this subsection.\n**(7) Staffing**\nThe Administrator shall ensure adequate staffing to conduct the safety reviews within the deadlines specified in this section.\n#### 7. FAA-DOD safety information sharing\n##### (a) MOU with the Department of the Army\nNot later than 60 days after the date of enactment of this section, the Administrator shall enter into a Memorandum of Understanding with the Secretary of the Army to permit, as appropriate, the sharing of information from the Army\u2019s Safety Management Information System with the FAA to facilitate communications and analysis of any applicable impacts to the safety and efficiency of civil aviation operations and to mitigate risk in the national airspace system.\n##### (b) Other DOD MOUs\nNot later than 90 days after the date of enactment of this section, the Administrator shall enter into a Memorandum of Understanding with the following military departments to permit, as appropriate, the sharing of information from applicable aviation safety information systems to facilitate communications and analysis of any applicable impacts to the safety and efficiency of civil aviation operations and to mitigate risk in the national airspace system:\n**(1)**\nThe Department of the Navy.\n**(2)**\nThe Department of the Air Force.\n**(3)**\nThe Coast Guard.\n##### (c) Congressional notification\nNot later than 7 days after the date on which the Administrator enters into any Memorandum of Understanding under subsection (a) or (b), the Administrator shall notify the Committee on Commerce, Science, and Transportation and the Committee on Armed Services of the Senate and the Committee on Transportation and Infrastructure and the Committee on Armed Services of the House of Representatives.\n#### 8. Repeal of provision regarding ADS\u2013B equipment on certain aircraft of department of defense\nSection 1046 of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( 49 U.S.C. 40101 note) is repealed.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2026-02-24",
        "actionTime": "14:05:16",
        "text": "On motion to suspend the rules and pass the bill Failed by the Yeas and Nays: (2/3 required): 264 - 133 (Roll no. 72)."
      },
      "number": "2503",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ROTOR Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-01-05T19:58:41Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-01-05T19:58:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-05T16:24:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6222",
          "measure-number": "6222",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-05-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6222v00",
            "update-date": "2026-05-16"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rotorcraft Operations Transparency and Oversight Reform Act or the ROTOR Act</strong></p><p>This bill addresses aviation safety by increasing\u00a0requirements for aircraft tracking and communication using Automatic Dependent Surveillance-Broadcast (ADS-B) technology and expanding oversight.</p><p>As background, ADS-B for broadcasting (Out) and receiving (In) transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In equipment to provide the aircraft with location information of other aircraft and traffic advisories. Current law does not require this equipment.</p><p>Current\u00a0Federal Aviation Administration (FAA) regulations\u00a0allow aircraft performing a sensitive government mission to\u00a0be excepted from requirements for using ADS-B Out equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights)\u00a0and requires\u00a0additional\u00a0reporting for the exception.</p><p>The Government Accountability Office must review the use of the ADS-B Out exception and the Office of Inspector General (OIG) of the Department of Transportation (DOT) must annually audit FAA oversight of operations that use the exception.\u00a0</p><p>Further, the bill repeals a 2018 law that prohibits DOT from requiring certain military aircraft to install or use ADS-B equipment.</p><p>The bill also requires</p><ul><li>the OIG of the Army to audit the Army\u2019s coordination with the FAA,</li><li>the FAA to establish an office to coordinate airspace usage of military aircraft and review the safety of flight operations and routes around airports, and</li><li>the FAA to enter into memoranda of understanding with military agencies for safety information sharing.</li></ul>"
        },
        "title": "ROTOR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6222.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rotorcraft Operations Transparency and Oversight Reform Act or the ROTOR Act</strong></p><p>This bill addresses aviation safety by increasing\u00a0requirements for aircraft tracking and communication using Automatic Dependent Surveillance-Broadcast (ADS-B) technology and expanding oversight.</p><p>As background, ADS-B for broadcasting (Out) and receiving (In) transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In equipment to provide the aircraft with location information of other aircraft and traffic advisories. Current law does not require this equipment.</p><p>Current\u00a0Federal Aviation Administration (FAA) regulations\u00a0allow aircraft performing a sensitive government mission to\u00a0be excepted from requirements for using ADS-B Out equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights)\u00a0and requires\u00a0additional\u00a0reporting for the exception.</p><p>The Government Accountability Office must review the use of the ADS-B Out exception and the Office of Inspector General (OIG) of the Department of Transportation (DOT) must annually audit FAA oversight of operations that use the exception.\u00a0</p><p>Further, the bill repeals a 2018 law that prohibits DOT from requiring certain military aircraft to install or use ADS-B equipment.</p><p>The bill also requires</p><ul><li>the OIG of the Army to audit the Army\u2019s coordination with the FAA,</li><li>the FAA to establish an office to coordinate airspace usage of military aircraft and review the safety of flight operations and routes around airports, and</li><li>the FAA to enter into memoranda of understanding with military agencies for safety information sharing.</li></ul>",
      "updateDate": "2026-05-16",
      "versionCode": "id119hr6222"
    },
    "title": "ROTOR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rotorcraft Operations Transparency and Oversight Reform Act or the ROTOR Act</strong></p><p>This bill addresses aviation safety by increasing\u00a0requirements for aircraft tracking and communication using Automatic Dependent Surveillance-Broadcast (ADS-B) technology and expanding oversight.</p><p>As background, ADS-B for broadcasting (Out) and receiving (In) transmits information (e.g., location and weather information) between aircraft and air traffic control.</p><p>Under the bill, aircraft must generally operate with ADS-B In equipment to provide the aircraft with location information of other aircraft and traffic advisories. Current law does not require this equipment.</p><p>Current\u00a0Federal Aviation Administration (FAA) regulations\u00a0allow aircraft performing a sensitive government mission to\u00a0be excepted from requirements for using ADS-B Out equipment. This bill limits which flights may be considered sensitive government missions (e.g., not training flights)\u00a0and requires\u00a0additional\u00a0reporting for the exception.</p><p>The Government Accountability Office must review the use of the ADS-B Out exception and the Office of Inspector General (OIG) of the Department of Transportation (DOT) must annually audit FAA oversight of operations that use the exception.\u00a0</p><p>Further, the bill repeals a 2018 law that prohibits DOT from requiring certain military aircraft to install or use ADS-B equipment.</p><p>The bill also requires</p><ul><li>the OIG of the Army to audit the Army\u2019s coordination with the FAA,</li><li>the FAA to establish an office to coordinate airspace usage of military aircraft and review the safety of flight operations and routes around airports, and</li><li>the FAA to enter into memoranda of understanding with military agencies for safety information sharing.</li></ul>",
      "updateDate": "2026-05-16",
      "versionCode": "id119hr6222"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6222ih.xml"
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
      "title": "ROTOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ROTOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rotorcraft Operations Transparency and Oversight Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require all aircraft to be equipped with Automatic Dependent Surveillance-Broadcast In, to improve aviation safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:48:27Z"
    }
  ]
}
```
