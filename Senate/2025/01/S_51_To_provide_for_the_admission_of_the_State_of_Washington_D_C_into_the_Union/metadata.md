# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/51?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/51
- Title: Washington, D.C. Admission Act
- Congress: 119
- Bill type: S
- Bill number: 51
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-05-27T19:49:33Z
- Update date including text: 2025-05-27T19:49:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/51",
    "number": "51",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Washington, D.C. Admission Act",
    "type": "S",
    "updateDate": "2025-05-27T19:49:33Z",
    "updateDateIncludingText": "2025-05-27T19:49:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:37:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "OR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Lujan",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NM"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "AZ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s51is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 51\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Van Hollen (for himself, Mr. Schumer , Mr. Peters , Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kim , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Ms. Smith , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , Mr. Wyden , Ms. Slotkin , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide for the admission of the State of Washington, D.C. into the Union.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Washington, D.C. Admission Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014State of Washington, D.C.\nSubtitle A\u2014Procedures for Admission\nSec. 101. Admission into the Union.\nSec. 102. Elections of Senators and Representative.\nSec. 103. Issuance of Presidential proclamation.\nSubtitle B\u2014Seat of Government of the United States\nSec. 111. Territory and boundaries.\nSec. 112. Description of Capital.\nSec. 113. Retention of title to property.\nSec. 114. Effect of admission on current laws of seat of Government of United States.\nSec. 115. Capital National Guard.\nSec. 116. Termination of legal status of seat of Government of United States as municipal corporation.\nSubtitle C\u2014General Provisions Relating to Laws of State\nSec. 121. Effect of admission on current laws.\nSec. 122. Pending actions and proceedings.\nSec. 123. Limitation on authority to tax Federal property.\nSec. 124. United States nationality.\nTitle II\u2014Interests of Federal Government\nSubtitle A\u2014Federal Property\nSec. 201. Treatment of military lands.\nSec. 202. Waiver of claims to Federal property.\nSubtitle B\u2014Federal Courts\nSec. 211. Residency requirements for certain Federal officials.\nSec. 212. Renaming of Federal courts.\nSec. 213. Conforming amendments relating to Department of Justice.\nSec. 214. Treatment of pretrial services in United States District Court.\nSubtitle C\u2014Federal Elections\nSec. 221. Permitting individuals residing in Capital to vote in Federal elections in State of most recent domicile.\nSec. 222. Repeal of Office of District of Columbia Delegate.\nSec. 223. Repeal of law providing for participation of seat of government in election of President and Vice President.\nSec. 224. Expedited procedures for consideration of constitutional amendment repealing 23rd Amendment.\nTitle III\u2014Continuation of Certain Authorities and Responsibilities\nSubtitle A\u2014Employee Benefits\nSec. 301. Federal benefit payments under certain retirement programs.\nSec. 302. Continuation of Federal civil service benefits for employees first employed prior to establishment of District of Columbia merit personnel system.\nSec. 303. Obligations of Federal Government under judges\u2019 retirement program.\nSubtitle B\u2014Agencies\nSec. 311. Public Defender Service.\nSec. 312. Prosecutions.\nSec. 313. Service of United States Marshals.\nSec. 314. Designation of felons to facilities of Bureau of Prisons.\nSec. 315. Parole and supervision.\nSec. 316. Courts.\nSubtitle C\u2014Other Programs and Authorities\nSec. 321. Application of the College Access Act.\nSec. 322. Application of the Scholarships for Opportunity and Results Act.\nSec. 323. Medicaid Federal medical assistance percentage.\nSec. 324. Federal planning commissions.\nSec. 325. Role of Army Corps of Engineers in supplying water.\nSec. 326. Requirements to be located in District of Columbia.\nTitle IV\u2014General Provisions\nSec. 401. General definitions.\nSec. 402. Statehood Transition Commission.\nSec. 403. Certification of enactment by President.\nSec. 404. Severability.\nI\nState of Washington, D.C.\nA\nProcedures for Admission\n#### 101. Admission into the Union\n##### (a) In general\nSubject to the provisions of this Act, upon the issuance of the proclamation required by section 103(a), the State of Washington, Douglass Commonwealth is declared to be a State of the United States of America, and is declared admitted into the Union on an equal footing with the other States in all respects whatever.\n##### (b) Constitution of State\nThe State Constitution shall always be republican in form and shall not be repugnant to the Constitution of the United States or the principles of the Declaration of Independence.\n##### (c) Nonseverability\nIf any provision of this section, or the application thereof to any person or circumstance, is held to be invalid, the remaining provisions of this Act and any amendments made by this Act shall be treated as invalid.\n#### 102. Elections of Senators and Representative\n##### (a) Issuance of proclamation\n**(1) In general**\nNot more than 30 days after receiving certification of the enactment of this Act from the President pursuant to section 403, the Mayor shall issue a proclamation for the first elections for 2 Senators and one Representative in Congress from the State, subject to the provisions of this section.\n**(2) Special rule for elections of Senators**\nIn the elections of Senators from the State pursuant to paragraph (1), the 2 Senate offices shall be separately identified and designated, and no person may be a candidate for both offices. No such identification or designation of either of the offices shall refer to or be taken to refer to the terms of such offices, or in any way impair the privilege of the Senate to determine the class to which each of the Senators shall be assigned.\n##### (b) Rules for conducting elections\n**(1) In general**\nThe proclamation of the Mayor issued under subsection (a) shall provide for the holding of a primary election and a general election, and in such elections the officers required to be elected as provided in subsection (a) shall be chosen by the qualified voters of the District of Columbia in the manner required by the laws of the District of Columbia.\n**(2) Certification of results**\nElection results shall be certified in the manner required by the laws of the District of Columbia, except that the Mayor shall also provide written certification of the results of such elections to the President.\n##### (c) Assumption of duties\nUpon the admission of the State into the Union, the Senators and Representative elected in the elections described in subsection (a) shall be entitled to be admitted to seats in Congress and to all the rights and privileges of Senators and Representatives of the other States in Congress.\n##### (d) Effect of admission on House of Representatives membership\n**(1) Permanent increase in number of Members**\nEffective with respect to the Congress during which the State is admitted into the Union and each succeeding Congress, the House of Representatives shall be composed of 436 Members, including any Members representing the State.\n**(2) Initial number of Representatives for State**\nUntil the taking effect of the first apportionment of Members occurring after the admission of the State into the Union, the State shall be entitled to one Representative in the House of Representatives upon its admission into the Union.\n**(3) Apportionment of Members resulting from admission of State**\n**(A) Apportionment**\nSection 22(a) of the Act entitled An Act to provide for the fifteenth and subsequent decennial censuses and to provide for apportionment of Representatives in Congress , approved June 18, 1929 ( 2 U.S.C. 2a(a) ), is amended by striking the then existing number of Representatives and inserting 436 Representatives .\n**(B) Effective date**\nThe amendment made by subparagraph (A) shall apply with respect to the first regular decennial census conducted after the admission of the State into the Union and each subsequent regular decennial census.\n#### 103. Issuance of Presidential proclamation\nThe President, upon the certification of the results of the elections of the officers required to be elected as provided in section 102(a), shall, not later than 90 days after receiving such certification pursuant to section 102(b)(2), issue a proclamation announcing the results of such elections as so ascertained.\nB\nSeat of Government of the United States\n#### 111. Territory and boundaries\n##### (a) In general\nExcept as provided in subsection (b), the State shall consist of all of the territory of the District of Columbia as of the date of the enactment of this Act, subject to the results of the metes and bounds survey conducted under subsection (c).\n##### (b) Exclusion of portion remaining as seat of Government of United States\nThe territory of the State shall not include the area described in section 112, which shall be known as the Capital and shall serve as the seat of the Government of the United States, as provided in clause 17 of section 8 of article I of the Constitution of the United States.\n##### (c) Metes and bounds survey\nNot later than 180 days after the date of the enactment of this Act, the President (in consultation with the Chair of the National Capital Planning Commission) shall conduct a metes and bounds survey of the Capital, as described in section 112(b).\n#### 112. Description of Capital\n##### (a) In general\nSubject to subsections (c) and (d), upon the admission of the State into the Union, the Capital shall consist of the property described in subsection (b) and shall include the principal Federal monuments, the White House, the Capitol Building, the United States Supreme Court Building, and the Federal executive, legislative, and judicial office buildings located adjacent to the Mall and the Capitol Building (as such terms are used in section 8501(a) of title 40, United States Code).\n##### (b) General description\nUpon the admission of the State into the Union, the boundaries of the Capital shall be as follows: Beginning at the intersection of the southern right-of-way of F Street NE and the eastern right-of-way of 2nd Street NE;\n**(1)**\nthence south along said eastern right-of-way of 2nd Street NE to its intersection with the northeastern right-of-way of Maryland Avenue NE;\n**(2)**\nthence southwest along said northeastern right-of-way of Maryland Avenue NE to its intersection with the northern right-of-way of Constitution Avenue NE;\n**(3)**\nthence west along said northern right-of-way of Constitution Avenue NE to its intersection with the eastern right-of-way of 1st Street NE;\n**(4)**\nthence south along said eastern right-of-way of 1st Street NE to its intersection with the southeastern right-of-way of Maryland Avenue NE;\n**(5)**\nthence northeast along said southeastern right-of-way of Maryland Avenue NE to its intersection with the eastern right-of-way of 2nd Street NE;\n**(6)**\nthence south along said eastern right-of-way of 2nd Street NE to the eastern right-of-way of 2nd Street SE;\n**(7)**\nthence south along said eastern right-of-way of 2nd Street SE to its intersection with the northern property boundary of the property designated as Square 760 Lot 803;\n**(8)**\nthence east along said northern property boundary of Square 760 Lot 803 to its intersection with the western right-of-way of 3rd Street SE;\n**(9)**\nthence south along said western right-of-way of 3rd Street SE to its intersection with the northern right-of-way of Independence Avenue SE;\n**(10)**\nthence west along said northern right-of-way of Independence Avenue SE to its intersection with the northeastern right-of-way of Pennsylvania Avenue SE;\n**(11)**\nthence northwest along said northeastern right-of-way of Pennsylvania Avenue SE to its intersection with the eastern right-of-way of 2nd Street SE;\n**(12)**\nthence south along said eastern right-of-way of 2nd Street SE to its intersection with the southern right-of-way of C Street SE;\n**(13)**\nthence west along said southern right-of-way of C Street SE to its intersection with the eastern right-of-way of 1st Street SE;\n**(14)**\nthence south along said eastern right-of-way of 1st Street SE to its intersection with the southern right-of-way of D Street SE;\n**(15)**\nthence west along said southern right-of-way of D Street SE to its intersection with the eastern right-of-way of South Capitol Street;\n**(16)**\nthence south along said eastern right-of-way of South Capitol Street to its intersection with the northeastern right-of-way of Canal Street SE;\n**(17)**\nthence southeast along said northeastern right-of-way of Canal Street SE to its intersection with the southern right-of-way of E Street SE;\n**(18)**\nthence east along said southern right-of-way of E Street SE to its intersection with the western right-of-way of 1st Street SE;\n**(19)**\nthence south along said western right-of-way of 1st Street SE to its intersection with the southernmost corner of the property designated as Square 736S Lot 801;\n**(20)**\nthence west along a line extended due west from said corner of said property designated as Square 736S Lot 801 to its intersection with the southwestern right-of-way of New Jersey Avenue SE;\n**(21)**\nthence southeast along said southwestern right-of-way of New Jersey Avenue SE to its intersection with the northeastern right-of-way of Virginia Avenue SE;\n**(22)**\nthence northwest along said northeastern right-of-way of Virginia Avenue SE to its intersection with the western right-of-way of South Capitol Street;\n**(23)**\nthence north along said western right-of-way of South Capitol Street to its intersection with the southern right-of-way of E Street SW;\n**(24)**\nthence west along said southern right-of-way of E Street SW to its end;\n**(25)**\nthence west along a line extending said southern right-of-way of E Street SW westward to its intersection with the eastern right-of-way of 2nd Street SW;\n**(26)**\nthence north along said eastern right-of-way of 2nd Street SW to its intersection with the southwestern right-of-way of Virginia Avenue SW;\n**(27)**\nthence northwest along said southwestern right-of-way of Virginia Avenue SW to its intersection with the western right-of-way of 3rd Street SW;\n**(28)**\nthence north along said western right-of-way of 3rd Street SW to its intersection with the northern right-of-way of D Street SW;\n**(29)**\nthence west along said northern right-of-way of D Street SW to its intersection with the eastern right-of-way of 4th Street SW;\n**(30)**\nthence north along said eastern right-of-way of 4th Street SW to its intersection with the northern right-of-way of C Street SW;\n**(31)**\nthence west along said northern right-of-way of C Street SW to its intersection with the eastern right-of-way of 6th Street SW;\n**(32)**\nthence north along said eastern right-of-way of 6th Street SW to its intersection with the northern right-of-way of Independence Avenue SW;\n**(33)**\nthence west along said northern right-of-way of Independence Avenue SW to its intersection with the western right-of-way of 12th Street SW;\n**(34)**\nthence south along said western right-of-way of 12th Street SW to its intersection with the northern right-of-way of D Street SW;\n**(35)**\nthence west along said northern right-of-way of D Street SW to its intersection with the eastern right-of-way of 14th Street SW;\n**(36)**\nthence south along said eastern right-of-way of 14th Street SW to its intersection with the northwestern boundary of the Consolidated Rail Corporation railroad easement;\n**(37)**\nthence southwest along said northwestern boundary of the Consolidated Rail Corporation railroad easement to its intersection with the eastern shore of the Potomac River;\n**(38)**\nthence generally northwest along said eastern shore of the Potomac River to its intersection with a line extending westward from the northern boundary of the property designated as Square 12 Lot 806;\n**(39)**\nthence east along said line extending westward from the northern boundary of the property designated as Square 12 Lot 806 to the northern boundary of the property designated as Square 12 Lot 806, and continuing east along the northern boundary of the property designated as Square 12 Lot 806 to its northeast corner;\n**(40)**\nthence east along a line extending east from said northeast corner of the property designated as Square 12 Lot 806 to its intersection with the western boundary of the property designated as Square 33 Lot 87;\n**(41)**\nthence south along said western boundary of the property designated as Square 33 Lot 87 to its intersection with the northwest corner of the property designated as Square 33 Lot 88;\n**(42)**\nthence counter-clockwise around the boundary of said property designated as Square 33 Lot 88 to its southeast corner, which is along the northern right-of-way of E Street NW;\n**(43)**\nthence east along said northern right-of-way of E Street NW to its intersection with the western right-of-way of 18th Street NW;\n**(44)**\nthence south along said western right-of-way of 18th Street NW to its intersection with the southwestern right-of-way of Virginia Avenue NW;\n**(45)**\nthence southeast along said southwestern right-of-way of Virginia Avenue NW to its intersection with the northern right-of-way of Constitution Avenue NW;\n**(46)**\nthence east along said northern right-of-way of Constitution Avenue NW to its intersection with the eastern right-of-way of 17th Street NW;\n**(47)**\nthence north along said eastern right-of-way of 17th Street NW to its intersection with the southern right-of-way of H Street NW;\n**(48)**\nthence east along said southern right-of-way of H Street NW to its intersection with the northwest corner of the property designated as Square 221 Lot 35;\n**(49)**\nthence counter-clockwise around the boundary of said property designated as Square 221 Lot 35 to its southeast corner, which is along the boundary of the property designated as Square 221 Lot 37;\n**(50)**\nthence counter-clockwise around the boundary of said property designated as Square 221 Lot 37 to its southwest corner, which it shares with the property designated as Square 221 Lot 42;\n**(51)**\nthence south along the boundary of said property designated as Square 221 Lot 42 to its southwest corner;\n**(52)**\nthence east along the southern border of said property designated as Square 221 Lot 42 to its intersection with the northwest corner of the property designated as Square 221 Lot 41;\n**(53)**\nthence south along the western boundary of said property designated as Square 221 Lot 41 to its southwest corner, which is along the northern right-of-way of Pennsylvania Avenue NW;\n**(54)**\nthence east along said northern right-of-way of Pennsylvania Avenue NW to its intersection with the western right-of-way of 15th Street NW;\n**(55)**\nthence south along said western right-of-way of 15th Street NW to its intersection with a line extending northwest from the southern right-of-way of the portion of Pennsylvania Avenue NW north of Pershing Square;\n**(56)**\nthence southeast along said line extending the southern right-of-way of Pennsylvania Avenue NW to the southern right-of-way of Pennsylvania Avenue NW, and continuing southeast along said southern right-of-way of Pennsylvania Avenue NW to its intersection with the western right-of-way of 14th Street NW;\n**(57)**\nthence south along said western right-of-way of 14th Street NW to its intersection with a line extending west from the southern right-of-way of D Street NW;\n**(58)**\nthence east along said line extending west from the southern right-of-way of D Street NW to the southern right-of-way of D Street NW, and continuing east along said southern right-of-way of D Street NW to its intersection with the eastern right-of-way of 13\u00bd Street NW;\n**(59)**\nthence north along said eastern right-of-way of 13\u00bd Street NW to its intersection with the southern right-of-way of Pennsylvania Avenue NW;\n**(60)**\nthence east and southeast along said southern right-of-way of Pennsylvania Avenue NW to its intersection with the western right-of-way of 12th Street NW;\n**(61)**\nthence south along said western right-of-way of 12th Street NW to its intersection with a line extending to the west from the southern boundary of the property designated as Square 324 Lot 809;\n**(62)**\nthence east along said line to the southwest corner of said property designated as Square 324 Lot 809, and continuing northeast along the southern boundary of said property designated as Square 324 Lot 809 to its eastern corner, which it shares with the property designated as Square 323 Lot 802;\n**(63)**\nthence east along the southern boundary of said property designated as Square 323 Lot 802 to its southeast corner, which it shares with the property designated as Square 324 Lot 808;\n**(64)**\nthence counter-clockwise around the boundary of said property designated as Square 324 Lot 808 to its northeastern corner, which is along the southern right-of-way of Pennsylvania Avenue NW;\n**(65)**\nthence southeast along said southern right-of-way of Pennsylvania Avenue NW to its intersection with the eastern right-of-way of 4th Street NW;\n**(66)**\nthence north along a line extending north from said eastern right-of-way of 4th Street NW to its intersection with the southern right-of-way of C Street NW;\n**(67)**\nthence east along said southern right-of-way of C Street NW to its intersection with the eastern right-of-way of 3rd Street NW;\n**(68)**\nthence north along said eastern right-of-way of 3rd Street NW to its intersection with the southern right-of-way of D Street NW;\n**(69)**\nthence east along said southern right-of-way of D Street NW to its intersection with the western right-of-way of 1st Street NW;\n**(70)**\nthence south along said western right-of-way of 1st Street NW to its intersection with the northern right-of-way of C Street NW;\n**(71)**\nthence west along said northern right-of-way of C Street NW to its intersection with the western right-of-way of 2nd Street NW;\n**(72)**\nthence south along said western right-of-way of 2nd Street NW to its intersection with the northern right-of-way of Constitution Avenue NW;\n**(73)**\nthence east along said northern right-of-way of Constitution Avenue NW to its intersection with the northwestern right-of-way of Louisiana Avenue NW;\n**(74)**\nthence northeast along said northwestern right-of-way of Louisiana Avenue NW to its intersection with the southwestern right-of-way of New Jersey Avenue NW;\n**(75)**\nthence northwest along said southwestern right-of-way of New Jersey Avenue NW to its intersection with the northern right-of-way of D Street NW;\n**(76)**\nthence east along said northern right-of-way of D Street NW to its intersection with the northwestern right-of-way of Louisiana Avenue NW;\n**(77)**\nthence northeast along said northwestern right-of-way of Louisiana Avenue NW to its intersection with the western right-of-way of North Capitol Street;\n**(78)**\nthence north along said western right-of-way of North Capitol Street to its intersection with the southwestern right-of-way of Massachusetts Avenue NW;\n**(79)**\nthence southeast along said southwestern right-of-way of Massachusetts Avenue NW to the southwestern right-of-way of Massachusetts Avenue NE;\n**(80)**\nthence southeast along said southwestern right-of-way of Massachusetts Avenue NE to the southern right-of-way of Columbus Circle NE;\n**(81)**\nthence counter-clockwise along said southern right-of-way of Columbus Circle NE to its intersection with the southern right-of-way of F Street NE; and\n**(82)**\nthence east along said southern right-of-way of F Street NE to the point of beginning.\n##### (c) Exclusion of building serving as State capitol\nNotwithstanding any other provision of this section, after the admission of the State into the Union, the Capital shall not be considered to include the building known as the John A. Wilson Building , as described and designated under section 601(a) of the Omnibus Spending Reduction Act of 1993 (sec. 10\u20131301(a), D.C. Official Code).\n##### (d) Clarification of treatment of Frances Perkins Building\nThe entirety of the Frances Perkins Building, including any portion of the Building which is north of D Street NW, shall be considered to be included in the Capital.\n#### 113. Retention of title to property\n##### (a) Retention of Federal title\nThe United States shall have and retain title to, or jurisdiction over, for purposes of administration and maintenance, all real and personal property with respect to which the United States holds title or jurisdiction for such purposes on the day before the date of the admission of the State into the Union.\n##### (b) Retention of State title\nThe State shall have and retain title to, or jurisdiction over, for purposes of administration and maintenance, all real and personal property with respect to which the District of Columbia holds title or jurisdiction for such purposes on the day before the date of the admission of the State into the Union.\n#### 114. Effect of admission on current laws of seat of Government of United States\nExcept as otherwise provided in this Act, the laws of the District of Columbia which are in effect on the day before the date of the admission of the State into the Union (without regard to whether such laws were enacted by Congress or by the District of Columbia) shall apply in the Capital in the same manner and to the same extent beginning on the date of the admission of the State into the Union, and shall be deemed laws of the United States which are applicable only in or to the Capital.\n#### 115. Capital National Guard\n##### (a) Establishment\nTitle 32, United States Code, is amended as follows:\n**(1) Definitions**\nIn paragraphs (4), (6), and (19) of section 101, by striking District of Columbia each place it appears and inserting Capital .\n**(2) Branches and organizations**\nIn section 103, by striking District of Columbia and inserting Capital .\n**(3) Units: location; organization; command**\nIn subsections (c) and (d) of section 104, by striking District of Columbia both places it appears and inserting Capital .\n**(4) Availability of appropriations**\nIn section 107(b), by striking District of Columbia and inserting Capital .\n**(5) Maintenance of other troops**\nIn subsections (a), (b), and (c) of section 109, by striking District of Columbia each place it appears and inserting Capital .\n**(6) Drug interdiction and counter-drug activities**\nIn section 112(h)\u2014\n**(A)**\nby striking District of Columbia, both places it appears and inserting Capital, ; and\n**(B)**\nin paragraph (2), by striking National Guard of the District of Columbia and inserting Capital National Guard .\n**(7) Enlistment oath**\nIn section 304, by striking District of Columbia and inserting Capital .\n**(8) Adjutants general**\nIn section 314, by striking District of Columbia each place it appears and inserting Capital .\n**(9) Detail of regular members of Army and Air Force to duty with National Guard**\nIn section 315, by striking District of Columbia each place it appears and inserting Capital .\n**(10) Discharge of officers; termination of appointment**\nIn section 324(b), by striking District of Columbia and inserting Capital .\n**(11) Relief from National Guard duty when ordered to active duty**\nIn subsections (a) and (b) of section 325, by striking District of Columbia each place it appears and inserting Capital .\n**(12) Courts-martial of National Guard not in Federal service: composition, jurisdiction, and procedures; convening authority**\nIn sections 326 and 327, by striking District of Columbia each place it appears and inserting Capital .\n**(13) Active Guard and Reserve duty: Governor's authority**\nIn section 328(a), by striking District of Columbia and inserting Capital .\n**(14) Training generally**\nIn section 501(b), by striking District of Columbia and inserting Capital .\n**(15) Participation in field exercises**\nIn section 503(b), by striking District of Columbia and inserting Capital .\n**(16) National Guard schools and small arms competitions**\nIn section 504(b), by striking District of Columbia and inserting Capital .\n**(17) Army and Air Force schools and field exercises**\nIn section 505, by striking National Guard of the District of Columbia and inserting Capital National Guard .\n**(18) National Guard Youth Challenge Program**\nIn subsections (c)(1), (g)(2), (j), (k), and (l)(1) of section 509, by striking District of Columbia each place it appears and inserting Capital .\n**(19) Issue of supplies**\nIn section 702\u2014\n**(A)**\nin subsection (a), by striking National Guard of the District of Columbia and inserting Capital National Guard ; and\n**(B)**\nin subsections (b), (c), and (d), by striking District of Columbia each place it appears and inserting Capital .\n**(20) Purchases of supplies from Army or Air Force**\nIn subsections (a) and (b) of section 703, by striking District of Columbia both places it appears and inserting Capital .\n**(21) Accountability: relief from upon order to active duty**\nIn section 704, by striking District of Columbia and inserting Capital .\n**(22) Property and fiscal officers**\nIn section 708\u2014\n**(A)**\nin subsection (a), by striking National Guard of the District of Columbia and inserting Capital National Guard ; and\n**(B)**\nin subsection (d), by striking District of Columbia and inserting Capital .\n**(23) Accountability for property issued to the National Guard**\nIn subsections (c), (d), (e), and (f) of section 710, by striking District of Columbia each place it appears and inserting Capital .\n**(24) Disposition of obsolete or condemned property**\nIn section 711, by striking District of Columbia and inserting Capital .\n**(25) Disposition of proceeds of condemned stores issued to National Guard**\nIn paragraph (1) of section 712, by striking District of Columbia and inserting Capital .\n**(26) Property loss; personal injury or death**\nIn section 715(c), by striking District of Columbia and inserting Capital .\n##### (b) Conforming amendments\n**(1) Capital defined**\n**(A) In general**\nSection 101 of title 32, United States Code, is amended by adding at the end the following new paragraph:\n(20) Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act. .\n**(B) With regards to Homeland Defense activities**\nSection 901 of title 32, United States Code, is amended\u2014\n**(i)**\nin paragraph (2), by striking District of Columbia and inserting Capital ; and\n**(ii)**\nby adding at the end the following new paragraph:\n(3) The term Governor means, with respect to the Capital, the commanding general of the Capital National Guard. .\n**(2) Title 10, United States Code**\nTitle 10, United States Code, is amended as follows:\n**(A) Definitions**\nIn section 101\u2014\n**(i)**\nin subsection (a), by adding at the end the following new paragraph:\n(21) The term Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act. ;\n**(ii)**\nin paragraphs (2) and (4) of subsection (c), by striking District of Columbia both places it appears and inserting Capital ; and\n**(iii)**\nin subsection (d)(5), by striking District of Columbia and inserting Capital .\n**(B) Disposition on discharge**\nIn section 771a(c), by striking District of Columbia and inserting Capital .\n**(C) TRICARE coverage for certain members of the National Guard and dependents during certain disaster response duty**\nIn section 1076f\u2014\n**(i)**\nin subsections (a) and (c)(1), by striking with respect to the District of Columbia, the mayor of the District of Columbia both places it appears and inserting with respect to the Capital, the commanding general of the Capital National Guard ; and\n**(ii)**\nin subsection (c)(2), by striking District of Columbia and inserting Capital .\n**(D) Payment of claims: availability of appropriations**\nIn paragraph (2)(B) of section 2732, by striking District of Columbia and inserting Capital .\n**(E) Members of Army National Guard: detail as students, observers, and investigators at educational institutions, industrial plants, and hospitals**\nIn section 7401(c), by striking District of Columbia and inserting Capital .\n**(F) Members of Air National Guard: detail as students, observers, and investigators at educational institutions, industrial plants, and hospitals**\nIn section 9401(c), by striking District of Columbia and inserting Capital .\n**(G) Ready Reserve: failure to satisfactorily perform prescribed training**\nIn section 10148(b)\u2014\n**(i)**\nby striking District of Columbia, and inserting Capital, ; and\n**(ii)**\nby striking District of Columbia National Guard and inserting Capital National Guard .\n**(H) Chief of the National Guard Bureau**\nIn section 10502(a)(1)\u2014\n**(i)**\nby striking District of Columbia, and inserting Capital, ; and\n**(ii)**\nby striking District of Columbia National Guard and inserting Capital National Guard .\n**(I) Vice Chief of the National Guard Bureau**\nIn section 10505(a)(1)(A)\u2014\n**(i)**\nby striking District of Columbia, and inserting Capital, ; and\n**(ii)**\nby striking District of Columbia National Guard and inserting Capital National Guard .\n**(J) Other senior National Guard Bureau officers**\nIn subparagraphs (A) and (B) of section 10506(a)(1)\u2014\n**(i)**\nby striking District of Columbia, both places it appears and inserting Capital, ; and\n**(ii)**\nby striking District of Columbia National Guard both places it appears and inserting Capital National Guard .\n**(K) National Guard Bureau: general provisions**\nIn section 10508(b)(1), by striking District of Columbia and inserting Capital .\n**(L) Commissioned officers: original appointment; limitation**\nIn section 12204(b), by striking District of Columbia and inserting Capital .\n**(M) Reserve components generally**\nIn section 12301(b), by striking District of Columbia National Guard both places it appears and inserting Capital National Guard .\n**(N) National Guard in Federal service: call**\nIn section 12406\u2014\n**(i)**\nby striking District of Columbia, and inserting Capital, ; and\n**(ii)**\nby striking National Guard of the District of Columbia and inserting Capital National Guard .\n**(O) Result of failure to comply with standards and qualifications**\nIn section 12642(c), by striking District of Columbia and inserting Capital .\n**(P) Limitation on relocation of National Guard units**\nIn section 18238\u2014\n**(i)**\nby striking District of Columbia, and inserting Capital, ; and\n**(ii)**\nby striking National Guard of the District of Columbia and inserting Capital National Guard .\n#### 116. Termination of legal status of seat of Government of United States as municipal corporation\nNotwithstanding section 2 of the Revised Statutes relating to the District of Columbia (sec. 1\u2013102, D.C. Official Code) or any other provision of law codified in subchapter I of chapter 1 of the District of Columbia Official Code, effective upon the date of the admission of the State into the Union, the Capital (or any portion thereof) shall not serve as a government and shall not be a body corporate for municipal purposes.\nC\nGeneral Provisions Relating to Laws of State\n#### 121. Effect of admission on current laws\n##### (a) Legislative power\nThe legislative power of the State shall extend to all rightful subjects of legislation in the State, consistent with the Constitution of the United States (including the restrictions and limitations imposed upon the States by article I, section 10) and subject to the provisions of this Act.\n##### (b) Continuation of authority and duties of members of executive, legislative, and judicial offices\nUpon the admission of the State into the Union, members of executive, legislative, and judicial offices of the District of Columbia shall be deemed members of the respective executive, legislative, and judicial offices of the State, as provided by the State Constitution and the laws of the State.\n##### (c) Treatment of Federal laws\nTo the extent that any law of the United States applies to the States generally, the law shall have the same force and effect in the State as elsewhere in the United States, except as such law may otherwise provide.\n##### (d) No effect on existing contracts\nNothing in the admission of the State into the Union shall affect any obligation under any contract or agreement under which the District of Columbia or the United States is a party, as in effect on the day before the date of the admission of the State into the Union.\n##### (e) Succession in interstate compacts\nThe State shall be deemed to be the successor to the District of Columbia for purposes of any interstate compact which is in effect on the day before the date of the admission of the State into the Union.\n##### (f) Continuation of service of Federal members on boards and commissions\nNothing in the admission of the State into the Union shall affect the authority of a representative of the Federal Government who, as of the day before the date of the admission of the State into the Union, is a member of a board or commission of the District of Columbia to serve as a member of such board or commission or as a member of a successor to such board or commission after the admission of the State into the Union, as may be provided by the State Constitution and the laws of the State.\n##### (g) Special rule regarding enforcement authority of United States Capitol Police, United States Park Police, and United States Secret Service Uniformed Division\nThe United States Capitol Police, the United States Park Police, and the United States Secret Service Uniformed Division may not enforce any law of the State in the State, except to the extent authorized by the State. Nothing in this subsection may be construed to affect the authority of the United States Capitol Police, the United States Park Police, and the United States Secret Service Uniformed Division to enforce any law in the Capital.\n#### 122. Pending actions and proceedings\n##### (a) State as legal successor to District of Columbia\nThe State shall be the legal successor to the District of Columbia in all matters.\n##### (b) No effect on pending proceedings\nAll existing writs, actions, suits, judicial and administrative proceedings, civil or criminal liabilities, prosecutions, judgments, sentences, orders, decrees, appeals, causes of action, claims, demands, titles, and rights shall continue unaffected by the admission of the State into the Union with respect to the State or the United States, except as may be provided under this Act, as may be modified in accordance with the provisions of the State Constitution, and as may be modified by the laws of the State or the United States, as the case may be.\n#### 123. Limitation on authority to tax Federal property\nThe State may not impose any tax on any real or personal property owned or acquired by the United States, except to the extent that Congress may permit.\n#### 124. United States nationality\nNo provision of this Act shall operate to confer United States nationality, to terminate nationality lawfully acquired, or to restore nationality terminated or lost under any law of the United States or under any treaty to which the United States is or was a party.\nII\nInterests of Federal Government\nA\nFederal Property\n#### 201. Treatment of military lands\n##### (a) Reservation of Federal authority\n**(1) In general**\nSubject to paragraph (2) and subsection (b) and notwithstanding the admission of the State into the Union, authority is reserved in the United States for the exercise by Congress of the power of exclusive legislation in all cases whatsoever over such tracts or parcels of land located in the State that, on the day before the date of the admission of the State into the Union, are controlled or owned by the United States and held for defense or Coast Guard purposes.\n**(2) Limitation on authority**\nThe power of exclusive legislation described in paragraph (1) shall vest and remain in the United States only so long as the particular tract or parcel of land involved is controlled or owned by the United States and held for defense or Coast Guard purposes.\n##### (b) Authority of State\n**(1) In general**\nThe reservation of authority in the United States under subsection (a) shall not operate to prevent such tracts or parcels of land from being a part of the State, or to prevent the State from exercising over or upon such lands, concurrently with the United States, any jurisdiction which it would have in the absence of such reservation of authority and which is consistent with the laws hereafter enacted by Congress pursuant to such reservation of authority.\n**(2) Service of process**\nThe State shall have the right to serve civil or criminal process in such tracts or parcels of land in which the authority of the United States is reserved under subsection (a) in suits or prosecutions for or on account of rights acquired, obligations incurred, or crimes committed in the State but outside of such lands.\n#### 202. Waiver of claims to Federal property\n##### (a) In general\nAs a compact with the United States, the State and its people disclaim all right and title to any real or personal property not granted or confirmed to the State by or under the authority of this Act, the right or title to which is held by the United States or subject to disposition by the United States.\n##### (b) Effect on claims against United States\n**(1) In general**\nNothing in this Act shall recognize, deny, enlarge, impair, or otherwise affect any claim against the United States, and any such claim shall be governed by applicable laws of the United States.\n**(2) Rule of construction**\nNothing in this Act is intended or shall be construed as a finding, interpretation, or construction by Congress that any applicable law authorizes, establishes, recognizes, or confirms the validity or invalidity of any claim referred to in paragraph (1), and the determination of the applicability to or the effect of any law on any such claim shall be unaffected by anything in this Act.\nB\nFederal Courts\n#### 211. Residency requirements for certain Federal officials\n##### (a) Circuit judges\nSection 44(c) of title 28, United States Code, is amended\u2014\n**(1)**\nby striking Except in the District of Columbia, each and inserting Each ; and\n**(2)**\nby striking within fifty miles of the District of Columbia and inserting within fifty miles of the Capital .\n##### (b) District judges\nSection 134(b) of such title is amended in the first sentence by striking the District of Columbia, the Southern District of New York, and and inserting the Southern District of New York and .\n##### (c) United States attorneys\nSection 545(a) of such title is amended by striking the first sentence and inserting Each United States attorney shall reside in the district for which he or she is appointed, except that those officers of the Southern District of New York and the Eastern District of New York may reside within 20 miles thereof. .\n##### (d) United States marshals\nSection 561(e)(1) of such title is amended to read as follows:\n(1) the marshal for the Southern District of New York may reside within 20 miles of the district; and .\n##### (e) Clerks of District Courts\nSection 751(c) of such title is amended by striking the District of Columbia and .\n##### (f) Effective date\nThe amendments made by this section shall apply only to individuals appointed after the date of the admission of the State into the Union.\n#### 212. Renaming of Federal courts\n##### (a) Renaming\n**(1) Circuit Court**\nSection 41 of title 28, United States Code, is amended\u2014\n**(A)**\nin the first column, by striking District of Columbia and inserting Capital ; and\n**(B)**\nin the second column, by striking District of Columbia and inserting Capital; Washington, Douglass Commonwealth .\n**(2) District Court**\nSection 88 of such title is amended\u2014\n**(A)**\nin the heading, by striking District of Columbia and inserting Washington, Douglass Commonwealth and the Capital ;\n**(B)**\nby amending the first paragraph to read as follows:\nThe State of Washington, Douglass Commonwealth and the Capital comprise one judicial district. ; and\n**(C)**\nin the second paragraph, by striking Washington and inserting the Capital .\n**(3) Clerical amendment**\nThe item relating to section 88 in the table of sections for chapter 5 of such title is amended to read as follows:\n88. Washington, Douglass Commonwealth and the Capital. .\n##### (b) Conforming amendments relating to Court of Appeals\nTitle 28, United States Code, is amended as follows:\n**(1) Appointment of judges**\nSection 44(a) of such title is amended in the first column by striking District of Columbia and inserting Capital .\n**(2) Terms of Court**\nSection 48(a) of such title is amended\u2014\n**(A)**\nin the first column, by striking District of Columbia and inserting Capital ;\n**(B)**\nin the second column, by striking Washington and inserting Capital ; and\n**(C)**\nin the second column, by striking District of Columbia and inserting Capital .\n**(3) Appointment of independent counsels by chief judge of circuit**\nSection 49 of such title is amended by striking District of Columbia each place it appears and inserting Capital .\n**(4) Circuit Court jurisdiction over certification of death penalty counsels**\nSection 2265(c)(2) of such title is amended by striking the District of Columbia Circuit and inserting the Capital Circuit .\n**(5) Circuit Court jurisdiction over review of Federal agency orders**\nSection 2343 of such title is amended by striking the District of Columbia Circuit and inserting the Capital Circuit .\n##### (c) Conforming amendments relating to District Court\nTitle 28, United States Code, is amended as follows:\n**(1) Appointment and number of District Court judges**\nSection 133(a) of such title is amended in the first column by striking District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(2) District Court jurisdiction of tax cases brought against United States**\nSection 1346(e) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(3) District Court jurisdiction over proceedings for forfeiture of foreign property**\nSection 1355(b)(2) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(4) District Court jurisdiction over civil actions brought against a foreign state**\nSection 1391(f)(4) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(5) District Court jurisdiction over actions brought by corporations against United States**\nSection 1402(a)(2) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(6) Venue in District Court of certain actions brought by employees of Executive Office of the President**\nSection 1413 of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(7) Venue in District Court of action enforcing foreign judgment**\nSection 2467(c)(2)(B) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n##### (d) Conforming amendments relating to other courts\nTitle 28, United States Code, is amended as follows:\n**(1) Appointment of bankruptcy judges**\nSection 152(a)(2) of such title is amended in the first column by striking District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n**(2) Location of Court of Federal Claims**\nSection 173 of such title is amended by striking the District of Columbia and inserting the Capital .\n**(3) Duty station of judges of Court of Federal Claims**\nSection 175 of such title is amended by striking the District of Columbia each place it appears and inserting the Capital .\n**(4) Duty station of judges for purposes of traveling expenses**\nSection 456(b) of such title is amended to read as follows:\n(b) The official duty station of the Chief Justice of the United States, the Justices of the Supreme Court of the United States, and the judges of the United States Court of Appeals for the Federal Circuit shall be the Capital. .\n**(5) Court accommodations for Federal Circuit and Court of Federal Claims**\nSection 462(d) of such title is amended by striking the District of Columbia and inserting the Capital .\n**(6) Places of holding court of Court of Federal Claims**\nSection 798(a) of such title is amended\u2014\n**(A)**\nby striking Washington, District of Columbia and inserting the Capital ; and\n**(B)**\nby striking the District of Columbia and inserting the Capital .\n##### (e) Other conforming amendments\n**(1) Service of process on foreign parties at State Department office**\nSection 1608(a)(4) of such title is amended by striking Washington, District of Columbia and inserting the Capital .\n**(2) Service of process in property cases at Attorney General office**\nSection 2410(b) of such title is amended by striking Washington, District of Columbia and inserting the Capital .\n##### (f) Definition\nSection 451 of title 28, United States Code, is amended by adding at the end the following new undesignated paragraph:\nThe term Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act. .\n##### (g) References in other laws\nAny reference in any Federal law (other than a law amended by this section), rule, or regulation\u2014\n**(1)**\nto the United States Court of Appeals for the District of Columbia shall be deemed to refer to the United States Court of Appeals for the Capital;\n**(2)**\nto the District of Columbia Circuit shall be deemed to refer to the Capital Circuit; and\n**(3)**\nto the United States District Court for the District of Columbia shall be deemed to refer to the United States District Court for Washington, Douglass Commonwealth and the Capital.\n##### (h) Effective date\nThis section and the amendments made by this section shall take effect upon the admission of the State into the Union.\n#### 213. Conforming amendments relating to Department of Justice\n##### (a) Appointment of United States Trustees\nSection 581(a)(4) of title 28, United States Code, is amended by striking the District of Columbia and inserting the Capital and Washington, Douglass Commonwealth .\n##### (b) Independent counsels\n**(1) Appointment of additional personnel**\nSection 594(c) of such title is amended\u2014\n**(A)**\nby striking the District of Columbia the first place it appears and inserting Washington, Douglass Commonwealth and the Capital ; and\n**(B)**\nby striking the District of Columbia the second place it appears and inserting Washington, Douglass Commonwealth .\n**(2) Judicial review of removal**\nSection 596(a)(3) of such title is amended by striking the District of Columbia and inserting Washington, Douglass Commonwealth and the Capital .\n##### (c) Effective date\nThe amendments made by this section shall take effect upon the admission of the State into the Union.\n#### 214. Treatment of pretrial services in United States District Court\nSection 3152 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking (other than the District of Columbia) and inserting (subject to subsection (d), other than the District of Columbia) ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) In the case of the judicial district of Washington, Douglass Commonwealth and the Capital\u2014 (1) upon the admission of the State of Washington, Douglass Commonwealth into the Union, the Washington, Douglass Commonwealth Pretrial Services Agency shall continue to provide pretrial services in the judicial district in the same manner and to the same extent as the District of Columbia Pretrial Services Agency provided such services in the judicial district of the District of Columbia as of the day before the date of the admission of the State into the Union; and (2) upon the receipt by the President of the certification from the State of Washington, Douglass Commonwealth under section 315(b)(4) of the Washington, D.C. Admission Act that the State has in effect laws providing for the State to provide pre-trial services, paragraph (1) shall no longer apply, and the Director shall provide for the establishment of pretrial services in the judicial district under this section. .\nC\nFederal Elections\n#### 221. Permitting individuals residing in Capital to vote in Federal elections in State of most recent domicile\n##### (a) Requirement for states To permit individuals To vote by absentee ballot\n**(1) In general**\nEach State shall\u2014\n**(A)**\npermit absent Capital voters to use absentee registration procedures and to vote by absentee ballot in general, special, primary, and runoff elections for Federal office; and\n**(B)**\naccept and process, with respect to any general, special, primary, or runoff election for Federal office, any otherwise valid voter registration application from an absent Capital voter, if the application is received by the appropriate State election official not less than 30 days before the election.\n**(2) Absent Capital voter defined**\nIn this section, the term absent Capital voter means, with respect to a State, a person who resides in the Capital and is qualified to vote in the State (or who would be qualified to vote in the State but for residing in the Capital), but only if the State is the last place in which the person was domiciled before residing in the Capital.\n**(3) State defined**\nIn this section, the term State means each of the several States, including the State.\n##### (b) Recommendations to States To maximize access to polls by absent Capital voters\nTo afford maximum access to the polls by absent Capital voters, it is the sense of Congress that the States should\u2014\n**(1)**\nwaive registration requirements for absent Capital voters who, by reason of residence in the Capital, do not have an opportunity to register;\n**(2)**\nexpedite processing of balloting materials with respect to such individuals; and\n**(3)**\nassure that absentee ballots are mailed to such individuals at the earliest opportunity.\n##### (c) Enforcement\nThe Attorney General may bring a civil action in the appropriate district court of the United States for such declaratory or injunctive relief as may be necessary to carry out this section.\n##### (d) Effect on certain other laws\nThe exercise of any right under this section shall not affect, for purposes of a Federal tax, a State tax, or a local tax, the residence or domicile of a person exercising such right.\n##### (e) Effective date\nThis section shall take effect upon the date of the admission of the State into the Union, and shall apply with respect to elections for Federal office taking place on or after such date.\n#### 222. Repeal of Office of District of Columbia Delegate\n##### (a) In General\nSections 202 and 204 of the District of Columbia Delegate Act ( Public Law 91\u2013405 ; sections 1\u2013401 and 1\u2013402, D.C. Official Code) are repealed, and the provisions of law amended or repealed by such sections are restored or revived as if such sections had not been enacted.\n##### (b) Conforming Amendments to District of Columbia Elections Code of 1955\nThe District of Columbia Elections Code of 1955 is amended\u2014\n**(1)**\nin section 1 (sec. 1\u20131001.01, D.C. Official Code), by striking the Delegate to the House of Representatives, ;\n**(2)**\nin section 2 (sec. 1\u20131001.02, D.C. Official Code)\u2014\n**(A)**\nby striking paragraph (6);\n**(B)**\nin paragraph (12), by striking (except the Delegate to Congress for the District of Columbia) ; and\n**(C)**\nin paragraph (13), by striking the Delegate to Congress for the District of Columbia, ;\n**(3)**\nin section 8 (sec. 1\u20131001.08, D.C. Official Code)\u2014\n**(A)**\nby striking Delegate, in the heading; and\n**(B)**\nby striking Delegate, each place it appears in subsections (d), (h)(1)(A), (h)(2), (i)(1), (j)(1), (j)(3), and (k)(3);\n**(4)**\nin section 10 (sec. 1\u20131001.10, D.C. Official Code)\u2014\n**(A)**\nby striking subparagraph (A) of subsection (a)(3); and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nby striking Delegate, each place it appears in paragraph (1); and\n**(ii)**\nby striking paragraph (2) and redesignating paragraph (3) as paragraph (2);\n**(5)**\nin section 11(a)(2) (sec. 1\u20131001.11(a)(2), D.C. Official Code), by striking Delegate to the House of Representatives, ;\n**(6)**\nin section 15(b) (sec. 1\u20131001.15(b), D.C. Official Code), by striking Delegate, ; and\n**(7)**\nin section 17(a) (sec. 1\u20131001.17(a), D.C. Official Code), by striking except the Delegate to the Congress from the District of Columbia .\n##### (c) Effective Date\nThe amendments made by this section shall take effect upon the admission of the State into the Union.\n#### 223. Repeal of law providing for participation of seat of government in election of President and Vice President\n##### (a) In general\nSection 21 of title 3, United States Code, is amended\u2014\n**(1)**\nby striking paragraph (2);\n**(2)**\nby redesignating paragraph (3) as paragraph (2); and\n**(3)**\nin paragraph (2), as so redesignated, by striking (or, in the case of the District of Columbia, the Mayor of the District of Columbia) .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect upon the date of the admission of the State into the Union, and shall apply to any election of the President and Vice President taking place on or after such date.\n#### 224. Expedited procedures for consideration of constitutional amendment repealing 23rd Amendment\n##### (a) Joint resolution described\nIn this section, the term joint resolution means a joint resolution\u2014\n**(1)**\nentitled A joint resolution proposing an amendment to the Constitution of the United States to repeal the 23rd article of amendment ; and\n**(2)**\nthe matter after the resolving clause of which consists solely of text to amend the Constitution of the United States to repeal the 23rd article of amendment to the Constitution.\n##### (b) Expedited consideration in House of Representatives\n**(1) Placement on calendar**\nUpon introduction in the House of Representatives, the joint resolution shall be placed immediately on the appropriate calendar.\n**(2) Proceeding to consideration**\n**(A) In general**\nIt shall be in order, not later than 30 legislative days after the date the joint resolution is introduced in the House of Representatives, to move to proceed to consider the joint resolution in the House of Representatives.\n**(B) Procedure**\nFor a motion to proceed to consider the joint resolution\u2014\n**(i)**\nall points of order against the motion are waived;\n**(ii)**\nsuch a motion shall not be in order after the House of Representatives has disposed of a motion to proceed on the joint resolution;\n**(iii)**\nthe previous question shall be considered as ordered on the motion to its adoption without intervening motion;\n**(iv)**\nthe motion shall not be debatable; and\n**(v)**\na motion to reconsider the vote by which the motion is disposed of shall not be in order.\n**(3) Consideration**\nWhen the House of Representatives proceeds to consideration of the joint resolution\u2014\n**(A)**\nthe joint resolution shall be considered as read;\n**(B)**\nall points of order against the joint resolution and against its consideration are waived;\n**(C)**\nthe previous question shall be considered as ordered on the joint resolution to its passage without intervening motion except 10 hours of debate equally divided and controlled by the proponent and an opponent;\n**(D)**\nan amendment to the joint resolution shall not be in order; and\n**(E)**\na motion to reconsider the vote on passage of the joint resolution shall not be in order.\n##### (c) Expedited consideration in Senate\n**(1) Placement on calendar**\nUpon introduction in the Senate, the joint resolution shall be placed immediately on the calendar.\n**(2) Proceeding to consideration**\n**(A) In general**\nNotwithstanding rule XXII of the Standing Rules of the Senate, it is in order, not later than 30 legislative days after the date the joint resolution is introduced in the Senate (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the joint resolution.\n**(B) Procedure**\nFor a motion to proceed to the consideration of the joint resolution\u2014\n**(i)**\nall points of order against the motion are waived;\n**(ii)**\nthe motion is not debatable;\n**(iii)**\nthe motion is not subject to a motion to postpone;\n**(iv)**\na motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order; and\n**(v)**\nif the motion is agreed to, the joint resolution shall remain the unfinished business until disposed of.\n**(3) Floor consideration**\n**(A) In general**\nIf the Senate proceeds to consideration of the joint resolution\u2014\n**(i)**\nall points of order against the joint resolution (and against consideration of the joint resolution) are waived;\n**(ii)**\nconsideration of the joint resolution, and all debatable motions and appeals in connection therewith, shall be limited to not more than 30 hours, which shall be divided equally between the majority and minority leaders or their designees;\n**(iii)**\na motion further to limit debate is in order and not debatable;\n**(iv)**\nan amendment to, a motion to postpone, or a motion to commit the joint resolution is not in order; and\n**(v)**\na motion to proceed to the consideration of other business is not in order.\n**(B) Vote on passage**\nIn the Senate the vote on passage shall occur immediately following the conclusion of the consideration of the joint resolution, and a single quorum call at the conclusion of the debate if requested in accordance with the rules of the Senate.\n**(C) Rulings of the Chair on procedure**\nAppeals from the decisions of the Chair relating to the application of this subsection or the rules of the Senate, as the case may be, to the procedure relating to the joint resolution shall be decided without debate.\n##### (d) Rules relating to Senate and House of Representatives\n**(1) Coordination with action by other House**\nIf, before the passage by one House of the joint resolution of that House, that House receives from the other House the joint resolution\u2014\n**(A)**\nthe joint resolution of the other House shall not be referred to a committee; and\n**(B)**\nwith respect to the joint resolution of the House receiving the resolution\u2014\n**(i)**\nthe procedure in that House shall be the same as if no joint resolution had been received from the other House; and\n**(ii)**\nthe vote on passage shall be on the joint resolution of the other House.\n**(2) Treatment of joint resolution of other House**\nIf one House fails to introduce or consider the joint resolution under this section, the joint resolution of the other House shall be entitled to expedited floor procedures under this section.\n**(3) Treatment of companion measures**\nIf, following passage of the joint resolution in the Senate, the Senate receives the companion measure from the House of Representatives, the companion measure shall not be debatable.\n##### (e) Rules of House of Representatives and Senate\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of the joint resolution, and supersede other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\nIII\nContinuation of Certain Authorities and Responsibilities\nA\nEmployee Benefits\n#### 301. Federal benefit payments under certain retirement programs\n##### (a) Continuation of entitlement to payments\nAny individual who, as of the day before the date of the admission of the State into the Union, is entitled to a Federal benefit payment under the District of Columbia Retirement Protection Act of 1997 (subtitle A of title XI of the National Capital Revitalization and Self-Government Improvement Act of 1997; sec. 1\u2013801.01 et seq., D.C. Official Code) shall continue to be entitled to such a payment after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such Act.\n##### (b) Obligations of Federal Government\n**(1) In general**\nAny obligation of the Federal Government under the District of Columbia Retirement Protection Act of 1997 which exists with respect to any individual or with respect to the District of Columbia as of the day before the date of the admission of the State into the Union shall remain in effect with respect to such an individual and with respect to the State after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such Act.\n**(2) D.C. Federal Pension Fund**\nAny obligation of the Federal Government under chapter 9 of the District of Columbia Retirement Protection Act of 1997 (sec. 1\u2013817.01 et seq., D.C. Official Code) with respect to the D.C. Federal Pension Fund which exists as of the day before the date of the admission of the State into the Union shall remain in effect with respect to such Fund after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such chapter.\n##### (c) Obligations of State\nAny obligation of the District of Columbia under the District of Columbia Retirement Protection Act of 1997 which exists with respect to any individual or with respect to the Federal Government as of the day before the date of the admission of the State into the Union shall become an obligation of the State with respect to such an individual and with respect to the Federal Government after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such Act.\n#### 302. Continuation of Federal civil service benefits for employees first employed prior to establishment of District of Columbia merit personnel system\n##### (a) Obligations of Federal Government\nAny obligation of the Federal Government under title 5, United States Code, which exists with respect to an individual described in subsection (c) or with respect to the District of Columbia as of the day before the date of the admission of the State into the Union shall remain in effect with respect to such individual and with respect to the State after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such title.\n##### (b) Obligations of State\nAny obligation of the District of Columbia under title 5, United States Code, which exists with respect to an individual described in subsection (c) or with respect to the Federal Government as of the day before the date of the admission of the State into the Union shall become an obligation of the State with respect to such individual and with respect to the Federal Government after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such title.\n##### (c) Individuals described\nAn individual described in this subsection is an individual who was first employed by the government of the District of Columbia before October 1, 1987.\n#### 303. Obligations of Federal Government under judges\u2019 retirement program\n##### (a) Continuation of obligations\n**(1) In general**\nAny obligation of the Federal Government under subchapter III of chapter 15 of title 11, District of Columbia Official Code\u2014\n**(A)**\nwhich exists with respect to any individual and the District of Columbia as the result of service accrued prior to the date of the admission of the State into the Union shall remain in effect with respect to such an individual and with respect to the State after the admission of the State into the Union, in the same manner, to the same extent, and subject to the same terms and conditions applicable under such subchapter; and\n**(B)**\nsubject to paragraph (2), shall exist with respect to any individual and the State as the result of service accrued after the date of the admission of the State into the Union in the same manner, to the same extent, and subject to the same terms and conditions applicable under such subchapter as such obligation existed with respect to individuals and the District of Columbia as of the date of the admission of the State into the Union.\n**(2) Treatment of service accrued after taking effect of State retirement program**\nSubparagraph (B) of paragraph (1) does not apply to service accrued on or after the termination date described in subsection (b).\n##### (b) Termination date\nThe termination date described in this subsection is the date on which the State provides written certification to the President that the State has in effect laws requiring the State to appropriate and make available funds for the retirement of judges of the State.\nB\nAgencies\n#### 311. Public Defender Service\n##### (a) Continuation of operations and funding\n**(1) In general**\nExcept as provided in paragraph (2) and subsection (b), title III of the District of Columbia Court Reform and Criminal Procedure Act of 1970 (sec. 2\u20131601 et seq., D.C. Official Code) shall apply with respect to the State and to the public defender service of the State after the date of the admission of the State into the Union in the same manner and to the same extent as such title applied with respect to the District of Columbia and the District of Columbia Public Defender Service as of the day before the date of the admission of the State into the Union.\n**(2) Responsibility for employer contribution**\nFor purposes of paragraph (2) of section 305(c) of such Act (sec. 2\u20131605(c)(2), D.C. Official Code), the Federal Government shall be treated as the employing agency with respect to the benefits provided under such section to an individual who is an employee of the public defender service of the State and who, pursuant to section 305(c) of such Act (sec. 2\u20131605(c), D.C. Official Code), is treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code.\n##### (b) Renaming of Service\nEffective upon the date of the admission of the State into the Union, the State may rename the public defender service of the State.\n##### (c) Continuation of Federal benefits for employees\n**(1) In general**\nAny individual who is an employee of the public defender service of the State as of the day before the date described in subsection (d) and who, pursuant to section 305(c) of the District of Columbia Court Reform and Criminal Procedure Act of 1970 (sec. 2\u20131605(c), D.C. Official Code), is treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code, shall continue to be treated as an employee of the Federal Government for such purposes, notwithstanding the termination of the provisions of subsection (a) under subsection (d).\n**(2) Responsibility for employer contribution**\nBeginning on the date described in subsection (d), the State shall be treated as the employing agency with respect to the benefits described in paragraph (1) which are provided to an individual who, for purposes of receiving such benefits, is continued to be treated as an employee of the Federal Government under such paragraph.\n##### (d) Termination\nSubsection (a) shall terminate upon the date on which the State provides written certification to the President that the State has in effect laws requiring the State to appropriate and make available funds for the operation of the office of the State which provides the services described in title III of the District of Columbia Court Reform and Criminal Procedure Act of 1970 (sec. 2\u20131601 et seq., D.C. Official Code).\n#### 312. Prosecutions\n##### (a) Assignment of Assistant United States attorneys\n**(1) In general**\nIn accordance with subchapter VI of chapter 33 of title 5, United States Code, the Attorney General, with the concurrence of the District of Columbia or the State (as the case may be), shall provide for the assignment of assistant United States attorneys to the State to carry out the functions described in subsection (b).\n**(2) Assignments made on detail without reimbursement by State**\nIn accordance with section 3373 of title 5, United States Code\u2014\n**(A)**\nan assistant United States attorney who is assigned to the State under this section shall be deemed under subsection (a) of such section to be on detail to a regular work assignment in the Department of Justice; and\n**(B)**\nthe assignment of an assistant United States attorney to the State under this section shall be made without reimbursement by the State of the pay of the attorney or any related expenses.\n##### (b) Functions described\nThe functions described in this subsection are criminal prosecutions conducted in the name of the State which would have been conducted in the name of the United States by the United States attorney for the District of Columbia or his or her assistants, as provided under section 23\u2013101(c), District of Columbia Official Code, but for the admission of the State into the Union.\n##### (c) Minimum number assigned\nThe number of assistant United States attorneys who are assigned under this section may not be less than the number of assistant United States attorneys whose principal duties as of the day before the date of the admission of the State into the Union were to conduct criminal prosecutions in the name of the United States under section 23\u2013101(c), District of Columbia Official Code.\n##### (d) Termination\nThe obligation of the Attorney General to provide for the assignment of assistant United States attorneys under this section shall terminate upon written certification by the State to the President that the State has appointed attorneys of the State to carry out the functions described in subsection (b).\n##### (e) Clarification regarding clemency authority\n**(1) In general**\nEffective upon the admission of the State into the Union, the authority to grant clemency for offenses against the District of Columbia or the State shall be exercised by such person or persons, and under such terms and conditions, as provided by the State Constitution and the laws of the State, without regard to whether the prosecution for the offense was conducted by the District of Columbia, the State, or the United States.\n**(2) Definition**\nIn this subsection, the term clemency means a pardon, reprieve, or commutation of sentence, or a remission of a fine or other financial penalty.\n#### 313. Service of United States Marshals\n##### (a) Provision of services for courts of State\nThe United States Marshals Service shall provide services with respect to the courts and court system of the State in the same manner and to the same extent as the Service provided services with respect to the courts and court system of the District of Columbia as of the day before the date of the admission of the State into the Union, except that the President shall not appoint a United States Marshal under section 561 of title 28, United States Code, for any court of the State.\n##### (b) Termination\nThe obligation of the United States Marshals Service to provide services under this section shall terminate upon written certification by the State to the President that the State has appointed personnel of the State to provide such services.\n#### 314. Designation of felons to facilities of Bureau of Prisons\n##### (a) Continuation of designation\nChapter 1 of subtitle C of title XI of the National Capital Revitalization and Self-Government Improvement Act of 1997 (sec. 24\u2013101 et seq., D.C. Official Code) and the amendments made by such chapter\u2014\n**(1)**\nshall continue to apply with respect to individuals convicted of offenses under the laws of the District of Columbia prior to the date of the admission of the State into the Union; and\n**(2)**\nshall apply with respect to individuals convicted of offenses under the laws of the State after the date of the admission of the State into the Union in the same manner and to the same extent as such chapter and amendments applied with respect to individuals convicted of offenses under the laws of the District of Columbia prior to the date of the admission of the State into the Union.\n##### (b) Termination\nThe provisions of this section shall terminate upon written certification by the State to the President that the State has in effect laws for the housing of individuals described in subsection (a) in correctional facilities.\n#### 315. Parole and supervision\n##### (a) United States Parole Commission\n**(1) Parole**\nThe United States Parole Commission\u2014\n**(A)**\nshall continue to exercise the authority to grant, deny, and revoke parole, and to impose conditions upon an order of parole, in the case of any individual who is an imprisoned felon who is eligible for parole or reparole under the laws of the District of Columbia as of the day before the date of the admission of the State into the Union, as provided under section 11231 of the National Capital Revitalization and Self-Government Improvement Act of 1997 (sec. 24\u2013131, D.C. Official Code); and\n**(B)**\nshall exercise the authority to grant, deny, and revoke parole, and to impose conditions upon an order of parole, in the case of any individual who is an imprisoned felon who is eligible for parole or reparole under the laws of the State in the same manner and to the same extent as the Commission exercised in the case of any individual described in subparagraph (A).\n**(2) Supervision of released offenders**\nThe United States Parole Commission\u2014\n**(A)**\nshall continue to exercise the authority over individuals who are released offenders of the District of Columbia as of the day before the date of the admission of the State into the Union, as provided under section 11233(c)(2) of the National Capital Revitalization and Self-Government Improvement Act of 1997 (sec. 24\u2013133(c)(2), D.C. Official Code); and\n**(B)**\nshall exercise authority over individuals who are released offenders of the State in the same manner and to the same extent as the Commission exercised authority over individuals described in subparagraph (A).\n**(3) Continuation of Federal benefits for employees**\n**(A) Continuation**\nAny individual who is an employee of the United States Parole Commission as of the later of the day before the date described in subparagraph (A) of paragraph (4) or the day before the date described in subparagraph (B) of paragraph (4) and who, on or after such date, is an employee of the office of the State which exercises the authority described in either such subparagraph, shall continue to be treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code, notwithstanding the termination of the provisions of this subsection under paragraph (4).\n**(B) Responsibility for employer contribution**\nBeginning on the later of the date described in subparagraph (A) of paragraph (4) or the date described in subparagraph (B) of paragraph (4), the State shall be treated as the employing agency with respect to the benefits described in subparagraph (A) which are provided to an individual who, for purposes of receiving such benefits, is continued to be treated as an employee of the Federal Government under such subparagraph.\n**(4) Termination**\nThe provisions of this subsection shall terminate\u2014\n**(A)**\nin the case of paragraph (1), on the date on which the State provides written certification to the President that the State has in effect laws providing for the State to exercise the authority to grant, deny, and revoke parole, and to impose conditions upon an order of parole, in the case of any individual who is an imprisoned felon who is eligible for parole or reparole under the laws of the State; and\n**(B)**\nin the case of paragraph (2), on the date on which the State provides written certification to the President that the State has in effect laws providing for the State to exercise authority over individuals who are released offenders of the State.\n##### (b) Court Services and Offender Supervision Agency\n**(1) Renaming**\nEffective upon the date of the admission of the State into the Union\u2014\n**(A)**\nthe Court Services and Offender Supervision Agency for the District of Columbia shall be known and designated as the Court Services and Offender Supervision Agency for Washington, Douglass Commonwealth, and any reference in any law, rule, or regulation to the Court Services and Offender Supervision Agency for the District of Columbia shall be deemed to refer to the Court Services and Offender Supervision Agency for Washington, Douglass Commonwealth; and\n**(B)**\nthe District of Columbia Pretrial Services Agency shall be known and designated as the Washington, Douglass Commonwealth Pretrial Services Agency, and any reference in any law, rule or regulation to the District of Columbia Pretrial Services Agency shall be deemed to refer to the Washington, Douglass Commonwealth Pretrial Services Agency.\n**(2) In general**\nThe Court Services and Offender Supervision Agency for Washington, Douglass Commonwealth, including the Washington, Douglass Commonwealth Pretrial Services Agency (as renamed under paragraph (1))\u2014\n**(A)**\nshall continue to provide pretrial services with respect to individuals who are charged with an offense in the District of Columbia, provide supervision for individuals who are offenders on probation, parole, and supervised release pursuant to the laws of the District of Columbia, and carry out sex offender registration functions with respect to individuals who are sex offenders in the District of Columbia, as of the day before the date of the admission of the State into the Union, as provided under section 11233 of the National Capital Revitalization and Self-Government Improvement Act of 1997 (sec. 24\u2013133, D.C. Official Code); and\n**(B)**\nshall provide pretrial services with respect to individuals who are charged with an offense in the State, provide supervision for offenders on probation, parole, and supervised release pursuant to the laws of the State, and carry out sex offender registration functions in the State, in the same manner and to the same extent as the Agency provided such services and supervision and carried out such functions for individuals described in subparagraph (A).\n**(3) Continuation of Federal benefits for employees**\n**(A) Continuation**\nAny individual who is an employee of the Court Services and Offender Supervision Agency for Washington, Douglass Commonwealth as of the day before the date described in paragraph (4), and who, on or after such date, is an employee of the office of the State which provides the services and carries out the functions described in paragraph (4), shall continue to be treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code, notwithstanding the termination of the provisions of paragraph (2) under paragraph (4).\n**(B) Responsibility for employer contribution**\nBeginning on the date described in paragraph (4), the State shall be treated as the employing agency with respect to the benefits described in subparagraph (A) which are provided to an individual who, for purposes of receiving such benefits, is continued to be treated as an employee of the Federal Government under such subparagraph.\n**(4) Termination**\nParagraph (2) shall terminate on the date on which the State provides written certification to the President that the State has in effect laws providing for the State to provide pretrial services, supervise offenders on probation, parole, and supervised release, and carry out sex offender registration functions in the State.\n#### 316. Courts\n##### (a) Continuation of operations\n**(1) In general**\nExcept as provided in paragraphs (2) and (3) and subsection (b), title 11, District of Columbia Official Code, as in effect on the day before the date of the admission of the State into the Union, shall apply with respect to the State and the courts and court system of the State after the date of the admission of the State into the Union in the same manner and to the same extent as such title applied with respect to the District of Columbia and the courts and court system of the District of Columbia as of the day before the date of the admission of the State into the Union.\n**(2) Responsibility for employer contribution**\nFor purposes of paragraph (2) of section 11\u20131726(b) and paragraph (2) of section 11\u20131726(c), District of Columbia Official Code, the Federal Government shall be treated as the employing agency with respect to the benefits provided under such section to an individual who is an employee of the courts and court system of the State and who, pursuant to either such paragraph, is treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code.\n**(3) Other exceptions**\n**(A) Selection of judges**\nEffective upon the date of the admission of the State into the Union, the State shall select judges for any vacancy on the courts of the State.\n**(B) Renaming of courts and other offices**\nEffective upon the date of the admission of the State into the Union, the State may rename any of its courts and any of the other offices of its court system.\n**(C) Rules of construction**\nNothing in this paragraph shall be construed\u2014\n**(i)**\nto affect the service of any judge serving on a court of the District of Columbia on the day before the date of the admission of the State into the Union, or to require the State to select such a judge for a vacancy on a court of the State; or\n**(ii)**\nto waive any of the requirements of chapter 15 of title 11, District of Columbia Official Code (other than section 11\u20131501(a) of such Code), including subchapter II of such chapter (relating to the District of Columbia Commission on Judicial Disabilities and Tenure), with respect to the appointment and service of judges of the courts of the State.\n##### (b) Continuation of Federal benefits for employees\n**(1) In general**\nAny individual who is an employee of the courts or court system of the State as of the day before the date described in subsection (e) and who, pursuant to section 11\u20131726(b) or section 11\u20131726(c), District of Columbia Official Code, is treated as an employee of the Federal Government for purposes of receiving benefits under any chapter of subpart G of part III of title 5, United States Code, shall continue to be treated as an employee of the Federal Government for such purposes, notwithstanding the termination of the provisions of this section under subsection (e).\n**(2) Responsibility for employer contribution**\nBeginning on the date described in subsection (e), the State shall be treated as the employing agency with respect to the benefits described in paragraph (1) which are provided to an individual who, for purposes of receiving such benefits, is continued to be treated as an employee of the Federal Government under such paragraph.\n##### (c) Continuation of funding\nSection 11241 of the National Capital Revitalization and Self-Government Improvement Act of 1997 (section 11\u20131743 note, District of Columbia Official Code) shall apply with respect to the State and the courts and court system of the State after the date of the admission of the State into the Union in the same manner and to the same extent as such section applied with respect to the Joint Committee on Judicial Administration in the District of Columbia and the courts and court system of the District of Columbia as of the day before the date of the admission of the State into the Union.\n##### (d) Treatment of court receipts\n**(1) Deposit of receipts into Treasury**\nExcept as provided in paragraph (2), all money received by the courts and court system of the State shall be deposited in the Treasury of the United States.\n**(2) Crime Victims Compensation Fund**\nSection 16 of the Victims of Violent Crime Compensation Act of 1996 (sec. 4\u2013515, D.C. Official Code), relating to the Crime Victims Compensation Fund, shall apply with respect to the courts and court system of the State in the same manner and to the same extent as such section applied to the courts and court system of the District of Columbia as of the day before the date of the admission of the State into the Union.\n##### (e) Termination\nThe provisions of this section, other than paragraph (3) of subsection (a) and except as provided under subsection (b), shall terminate on the date on which the State provides written certification to the President that the State has in effect laws requiring the State to appropriate and make available funds for the operation of the courts and court system of the State.\nC\nOther Programs and Authorities\n#### 321. Application of the College Access Act\n##### (a) Continuation\nThe District of Columbia College Access Act of 1999 ( Public Law 106\u201398 ; sec. 38\u20132701 et seq., D.C. Official Code) shall apply with respect to the State, and to the public institution of higher education designated by the State as the successor to the University of the District of Columbia, after the date of the admission of the State into the Union in the same manner and to the same extent as such Act applied with respect to the District of Columbia and the University of the District of Columbia as of the day before the date of the admission of the State into the Union.\n##### (b) Termination\nThe provisions of this section, other than with respect to the public institution of higher education designated by the State as the successor to the University of the District of Columbia, shall terminate upon written certification by the State to the President that the State has in effect laws requiring the State to provide tuition assistance substantially similar to the assistance provided under the District of Columbia College Access Act of 1999.\n#### 322. Application of the Scholarships for Opportunity and Results Act\n##### (a) Continuation\nThe Scholarships for Opportunity and Results Act (division C of Public Law 112\u201310 ; sec. 38\u20131853.01 et seq., D.C. Official Code) shall apply with respect to the State after the date of the admission of the State into the Union in the same manner and to the same extent as such Act applied with respect to the District of Columbia as of the day before the date of the admission of the State into the Union.\n##### (b) Termination\nThe provisions of this section shall terminate upon written certification by the State to the President that the State has in effect laws requiring the State\u2014\n**(1)**\nto provide tuition assistance substantially similar to the assistance provided under the Scholarships for Opportunity and Results Act; and\n**(2)**\nto provide supplemental funds to the public schools and public charter schools of the State in the amounts provided in the most recent fiscal year for public schools and public charter schools of the State or the District of Columbia (as the case may be) under such Act.\n#### 323. Medicaid Federal medical assistance percentage\n##### (a) Continuation\nNotwithstanding section 1905(b) of the Social Security Act ( 42 U.S.C. 1396d(b) ), during the period beginning on the date of the admission of the State into the Union and ending on September 30 of the fiscal year during which the State submits the certification described in subsection (b), the Federal medical assistance percentage for the State under title XIX of such Act shall be the Federal medical assistance percentage for the District of Columbia under such title as of the day before the date of the admission of the State into the Union.\n##### (b) Termination\nThe certification described in this subsection is a written certification by the State to the President that, during each of the first 5 fiscal years beginning after the date of the certification, the estimated revenues of the State will be sufficient to cover any reduction in revenues which may result from the termination of the provisions of this section.\n#### 324. Federal planning commissions\n##### (a) National Capital Planning Commission\n**(1) Continuing application**\nSubject to the amendments made by paragraphs (2) and (3), upon the admission of the State into the Union, chapter 87 of title 40, United States Code, shall apply as follows:\n**(A)**\nSuch chapter shall apply with respect to the Capital in the same manner and to the same extent as such chapter applied with respect to the District of Columbia as of the day before the date of the admission of the State into the Union.\n**(B)**\nSuch chapter shall apply with respect to the State in the same manner and to the same extent as such chapter applied with respect to the State of Maryland and the Commonwealth of Virginia as of the day before the date of the admission of the State into the Union.\n**(2) Composition of National Capital Planning Commission**\nSection 8711(b) of title 40, United States Code, is amended\u2014\n**(A)**\nby amending subparagraph (B) of paragraph (1) to read as follows:\n(B) four citizens with experience in city or regional planning, who shall be appointed by the President. ; and\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Residency requirement Of the four citizen members, one shall be a resident of Virginia, one shall be a resident of Maryland, and one shall be a resident of Washington, Douglass Commonwealth. .\n**(3) Conforming amendments to definitions of terms**\n**(A) Environs**\nParagraph (1) of section 8702 of such title is amended by striking the territory surrounding the District of Columbia and inserting the territory surrounding the National Capital .\n**(B) National Capital**\nParagraph (2) of section 8702 of such title is amended to read as follows:\n(2) National Capital The term National Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act, and the territory the Federal Government owns in the environs. .\n**(C) National Capital Region**\nSubparagraph (A) of paragraph (3) of section 8702 of such title is amended to read as follows:\n(A) the National Capital and the State of Washington, Douglass Commonwealth; .\n##### (b) Commission of Fine Arts\n**(1) Limiting application to the Capital**\nSection 9102(a)(1) of title 40, United States Code, is amended by striking the District of Columbia and inserting the Capital .\n**(2) Definition**\nSection 9102 of such title is amended by adding at the end the following new subsection:\n(d) Definition In this chapter, the term Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act. .\n**(3) Conforming amendment**\nSection 9101(d) of such title is amended by striking the District of Columbia and inserting the Capital .\n##### (c) Commemorative Works Act\n**(1) Limiting application to Capital**\nSection 8902 of title 40, United States Code, is amended by adding at the end the following new subsection:\n(c) Limiting application to Capital This chapter applies only with respect to commemorative works in the Capital and its environs. .\n**(2) Definition**\nParagraph (2) of section 8902(a) of such title is amended to read as follows:\n(2) Capital and its environs The term Capital and its environs means\u2014 (A) the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act; and (B) those lands and properties administered by the National Park Service and the General Services Administration located in the Reserve, Area I, and Area II as depicted on the map entitled Commemorative Areas Washington, DC and Environs , numbered 869/86501 B, and dated June 24, 2003, that are located outside of the State of Washington, Douglass Commonwealth. .\n**(3) Temporary site designation**\nSection 8907(a) of such title is amended by striking the District of Columbia and inserting the Capital and its environs .\n**(4) General conforming amendments**\nChapter 89 of such title is amended by striking the District of Columbia and its environs each place it appears in the following sections and inserting the Capital and its environs :\n**(A)**\nSection 8901(2) and 8901(4).\n**(B)**\nSection 8902(a)(4).\n**(C)**\nSection 8903(d).\n**(D)**\nSection 8904(c).\n**(E)**\nSection 8905(a).\n**(F)**\nSection 8906(a).\n**(G)**\nSection 8909(a) and 8909(b).\n**(5) Additional conforming amendment**\nSection 8901(2) of such title is amended by striking the urban fabric of the District of Columbia and inserting the urban fabric of the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act .\n##### (d) Effective date\nThis section and the amendments made by this section shall take effect on the date of the admission of the State into the Union.\n#### 325. Role of Army Corps of Engineers in supplying water\n##### (a) Continuation of role\nChapter 95 of title 40, United States Code, is amended by adding at the end the following new section:\n9508. Applicability to Capital and State of Washington, Douglass Commonwealth (a) In general Effective upon the admission of the State of Washington, Douglass Commonwealth into the Union, any reference in this chapter to the District of Columbia shall be deemed to refer to the Capital or the State of Washington, Douglass Commonwealth, as the case may be. (b) Definition In this section, the term Capital means the area serving as the seat of the Government of the United States, as described in section 112 of the Washington, D.C. Admission Act. .\n##### (b) Clerical amendment\nThe table of sections of chapter 95 of such title is amended by adding at the end the following:\n9508. Applicability to Capital and State of Washington, Douglass Commonwealth. .\n#### 326. Requirements to be located in District of Columbia\nThe location of any person in the Capital or Washington, Douglass Commonwealth on the day after the date of the admission of the State into the Union shall be deemed to satisfy any requirement under any law in effect as of the day before the date of the admission of the State into the Union that the person be located in the District of Columbia, including the requirements of section 72 of title 4, United States Code (relating to offices of the seat of the Government of the United States), and title 36, United States Code (relating to patriotic and national organizations).\nIV\nGeneral Provisions\n#### 401. General definitions\nIn this Act, the following definitions shall apply:\n**(1)**\nThe term Capital means the area serving as the seat of the Government of the United States, as described in section 112.\n**(2)**\nThe term Council means the Council of the District of Columbia.\n**(3)**\nThe term Mayor means the Mayor of the District of Columbia.\n**(4)**\nExcept as otherwise provided, the term State means the State of Washington, Douglass Commonwealth.\n**(5)**\nThe term State Constitution means the proposed Constitution of the State of Washington, D.C., as approved by the Council on October 18, 2016, pursuant to the Constitution and Boundaries for the State of Washington, D.C. Approval Resolution of 2016 (D.C. Resolution R21\u2013621), ratified by District of Columbia voters in Advisory Referendum B approved on November 8, 2016, and certified by the District of Columbia Board of Elections on November 18, 2016.\n#### 402. Statehood Transition Commission\n##### (a) Establishment\nThere is established the Statehood Transition Commission (hereafter in this section referred to as the Commission ).\n##### (b) Composition\n**(1) In general**\nThe Commission shall be composed of 18 members as follows:\n**(A)**\nThree members appointed by the President.\n**(B)**\nTwo members appointed by the Speaker of the House of Representatives.\n**(C)**\nTwo members appointed by the Minority Leader of the House of Representatives.\n**(D)**\nTwo members appointed by the Majority Leader of the Senate.\n**(E)**\nTwo members appointed by the Minority Leader of the Senate.\n**(F)**\nThree members appointed by the Mayor.\n**(G)**\nThree members appointed by the Council.\n**(H)**\nThe Chief Financial Officer of the District of Columbia.\n**(2) Appointment date**\n**(A) In general**\nThe appointments of the members of the Commission shall be made not later than 90 days after the date of the enactment of this Act.\n**(B) Effect of lack of appointment by appointment date**\nIf one or more appointments under any of the subparagraphs of paragraph (1) is not made by the appointment date specified in subparagraph (A), the authority to make such appointment or appointments shall expire, and the number of members of the Commission shall be reduced by the number equal to the number of appointments so not made.\n**(3) Term of service**\nEach member shall be appointed for the life of the Commission.\n**(4) Vacancy**\nA vacancy in the Commission shall be filled in the manner in which the original appointment was made.\n**(5) No compensation**\nMembers shall serve without pay, but shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n**(6) Chair and vice chair**\nThe Chair and Vice Chair of the Commission shall be elected by the members of the Commission\u2014\n**(A)**\nwith respect to the Chair, from among the members described in subparagraphs (A) through (E) of paragraph (1); and\n**(B)**\nwith respect to the Vice Chair, from among the members described in subparagraphs (F) and (G) of paragraph (1).\n##### (c) Staff\n**(1) Director**\nThe Commission shall have a Director, who shall be appointed by the Chair.\n**(2) Other staff**\nThe Director may appoint and fix the pay of such additional personnel as the Director considers appropriate.\n**(3) Non-applicability of certain civil service laws**\nThe Director and staff of the Commission may be appointed without regard to the provisions of title 5, United States Code, governing appointments in the competitive service, and may be paid without regard to the provisions of chapter 51 and subchapter III of chapter 53 of that title relating to classification and General Schedule pay rates, except that an individual so appointed may not receive pay in excess of the rate payable for level V of the Executive Schedule under section 5316 of such title.\n**(4) Experts and consultants**\nThe Commission may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals not to exceed the daily equivalent of the rate payable for level V of the Executive Schedule under section 5316 of such title.\n##### (d) Duties\nThe Commission shall advise the President, Congress, the Mayor (or, upon the admission of the State into the Union, the chief executive officer of the State), and the Council (or, upon the admission of the State into the Union, the legislature of the State) concerning an orderly transition to statehood for the District of Columbia or the State (as the case may be) and to a reduced geographical size of the seat of the Government of the United States, including with respect to property, funding, programs, projects, and activities.\n##### (e) Powers\n**(1) Hearings and sessions**\nThe Commission may, for the purpose of carrying out this Act, hold hearings, sit and act at times and places, take testimony, and receive evidence as the Commission considers appropriate.\n**(2) Obtaining official data**\nThe Commission may secure directly from any department or agency of the United States information necessary to enable it to carry out this Act. Upon request of the Chair of the Commission, the head of that department or agency shall furnish that information to the Commission.\n**(3) Mails**\nThe Commission may use the United States mails in the same manner and under the same conditions as other departments and agencies of the United States.\n**(4) Administrative support services**\nUpon the request of the Commission, the Administrator of General Services shall provide to the Commission the administrative support services necessary for the Commission to carry out its responsibilities under this Act.\n##### (f) Meetings\n**(1) In general**\nThe Commission shall meet at the call of the Chair.\n**(2) Initial meeting**\nThe Commission shall hold its first meeting not later than the earlier of\u2014\n**(A)**\n30 days after the date on which all members of the Commission have been appointed; or\n**(B)**\nif the number of members of the Commission is reduced under subsection (b)(2)(B), 90 days after the date of the enactment of this Act.\n**(3) Quorum**\nA majority of the members of the Commission shall constitute a quorum, but a lesser number of members may hold hearings.\n##### (g) Reports\nThe Commission shall submit such reports as the Commission considers appropriate or as may be requested by the President, Congress, or the District of Columbia (or, upon the admission of the State into the Union, the State).\n##### (h) Termination\nThe Commission shall cease to exist 2 years after the date of the admission of the State into the Union.\n#### 403. Certification of enactment by President\nNot more than 60 days after the date of the enactment of this Act, the President shall provide written certification of such enactment to the Mayor.\n#### 404. Severability\nExcept as provided in section 101(c), if any provision of this Act or amendment made by this Act, or the application thereof to any person or circumstance, is held to be invalid, the remaining provisions of this Act and any amendments made by this Act shall not be affected by the holding.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committees on Rules, Armed Services, the Judiciary, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "51",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Washington, D.C. Admission Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional districts and representation",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Congressional elections",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-19T20:53:46Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-19T20:53:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T13:35:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "Senate",
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
          "measure-id": "id119s51",
          "measure-number": "51",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s51v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Washington, D.C. Admission Act</strong></p><p>This bill provides for the establishment of the State of Washington, Douglass Commonwealth, and its admission into the United States.</p><p>The state is composed of most of the territory of the District of Columbia (DC), excluding a specified area that encompasses the U.S. Capitol, the White House, the U.S. Supreme Court building, federal monuments,\u00a0and federal office\u00a0buildings adjacent to the National Mall and the U.S. Capitol. The excluded territory shall be known as the Capital and serve as the seat of the government of the United States, as provided for in Article I of the Constitution. The state may not impose taxes on federal property except as Congress permits.</p><p>The bill provides for the DC Mayor to issue a proclamation for the first elections to Congress of two Senators and one Representative of the state.\u00a0The bill eliminates the office of Delegate to the House of Representatives.</p><p>The bill applies current DC laws to the state. DC judicial proceedings and contractual\u00a0obligations shall continue under the state\u2019s authority. The bill also provides for specified federal obligations to transfer to the state upon its certification that it has funds and laws in place to assume the obligations. These include maintaining a retirement fund for judges and operating public defender services.\u00a0</p><p>The bill establishes a commission that is generally\u00a0comprised of members who are appointed by\u00a0DC and federal government officials to advise on an orderly transition to statehood.</p>"
        },
        "title": "Washington, D.C. Admission Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s51.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Washington, D.C. Admission Act</strong></p><p>This bill provides for the establishment of the State of Washington, Douglass Commonwealth, and its admission into the United States.</p><p>The state is composed of most of the territory of the District of Columbia (DC), excluding a specified area that encompasses the U.S. Capitol, the White House, the U.S. Supreme Court building, federal monuments,\u00a0and federal office\u00a0buildings adjacent to the National Mall and the U.S. Capitol. The excluded territory shall be known as the Capital and serve as the seat of the government of the United States, as provided for in Article I of the Constitution. The state may not impose taxes on federal property except as Congress permits.</p><p>The bill provides for the DC Mayor to issue a proclamation for the first elections to Congress of two Senators and one Representative of the state.\u00a0The bill eliminates the office of Delegate to the House of Representatives.</p><p>The bill applies current DC laws to the state. DC judicial proceedings and contractual\u00a0obligations shall continue under the state\u2019s authority. The bill also provides for specified federal obligations to transfer to the state upon its certification that it has funds and laws in place to assume the obligations. These include maintaining a retirement fund for judges and operating public defender services.\u00a0</p><p>The bill establishes a commission that is generally\u00a0comprised of members who are appointed by\u00a0DC and federal government officials to advise on an orderly transition to statehood.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s51"
    },
    "title": "Washington, D.C. Admission Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Washington, D.C. Admission Act</strong></p><p>This bill provides for the establishment of the State of Washington, Douglass Commonwealth, and its admission into the United States.</p><p>The state is composed of most of the territory of the District of Columbia (DC), excluding a specified area that encompasses the U.S. Capitol, the White House, the U.S. Supreme Court building, federal monuments,\u00a0and federal office\u00a0buildings adjacent to the National Mall and the U.S. Capitol. The excluded territory shall be known as the Capital and serve as the seat of the government of the United States, as provided for in Article I of the Constitution. The state may not impose taxes on federal property except as Congress permits.</p><p>The bill provides for the DC Mayor to issue a proclamation for the first elections to Congress of two Senators and one Representative of the state.\u00a0The bill eliminates the office of Delegate to the House of Representatives.</p><p>The bill applies current DC laws to the state. DC judicial proceedings and contractual\u00a0obligations shall continue under the state\u2019s authority. The bill also provides for specified federal obligations to transfer to the state upon its certification that it has funds and laws in place to assume the obligations. These include maintaining a retirement fund for judges and operating public defender services.\u00a0</p><p>The bill establishes a commission that is generally\u00a0comprised of members who are appointed by\u00a0DC and federal government officials to advise on an orderly transition to statehood.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s51"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s51is.xml"
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
      "title": "Washington, D.C. Admission Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Washington, D.C. Admission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the admission of the State of Washington, D.C. into the Union.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T02:48:29Z"
    }
  ]
}
```
