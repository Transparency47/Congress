# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3991
- Title: DISCLOSE Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3991
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-04-24T14:21:24Z
- Update date including text: 2026-04-24T14:21:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3991",
    "number": "3991",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "DISCLOSE Act of 2026",
    "type": "S",
    "updateDate": "2026-04-24T14:21:24Z",
    "updateDateIncludingText": "2026-04-24T14:21:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
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
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T21:19:01Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "WA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "RI"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "WA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-04",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NH"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "WI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NM"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-04",
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
      "sponsorshipDate": "2026-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NH"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NV"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MN"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sponsorshipDate": "2026-03-04",
      "state": "CO"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "VT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "DE"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3991is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3991\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Whitehouse (for himself, Mr. Wyden , Mr. Schumer , Mr. Van Hollen , Ms. Klobuchar , Mr. Padilla , Mrs. Murray , Mr. Durbin , Mr. Reed , Ms. Cantwell , Mr. Sanders , Mrs. Shaheen , Mr. Warner , Mr. Merkley , Mr. Bennet , Mrs. Gillibrand , Mr. Coons , Mr. Blumenthal , Mr. Schatz , Ms. Baldwin , Mr. Murphy , Ms. Hirono , Mr. Heinrich , Mr. King , Mr. Kaine , Ms. Warren , Mr. Markey , Mr. Booker , Mr. Peters , Ms. Duckworth , Ms. Hassan , Ms. Cortez Masto , Ms. Smith , Ms. Rosen , Mr. Kelly , Mr. Luj\u00e1n , Mr. Hickenlooper , Mr. Ossoff , Mr. Warnock , Mr. Welch , Mr. Fetterman , Mr. Schiff , Mr. Kim , Mr. Gallego , Ms. Blunt Rochester , Ms. Slotkin , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to provide for additional disclosure requirements for corporations, labor organizations, Super PACs and other entities, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Democracy Is Strengthened by Casting Light On Spending in Elections Act of 2026 or the DISCLOSE Act of 2026 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nTITLE I\u2014Closing Loopholes Allowing Spending by Foreign Nationals in Elections\nSec. 101. Clarification of application of foreign money ban to certain disbursements and activities.\nSec. 102. Study and report on illicit foreign money in Federal elections.\nSec. 103. Prohibition on contributions and donations by foreign nationals in connection with ballot initiatives and referenda.\nSec. 104. Disbursements and activities subject to foreign money ban.\nSec. 105. Prohibiting establishment of corporation to conceal election contributions and donations by foreign nationals.\nTITLE II\u2014Reporting of Campaign-Related Disbursements\nSec. 201. Reporting of campaign-related disbursements.\nSec. 202. Reporting of Federal judicial nomination disbursements.\nSec. 203. Coordination with FinCEN.\nSec. 204. Application of foreign money ban to disbursements for campaign-related disbursements consisting of covered transfers.\nSec. 205. Sense of Congress regarding implementation.\nSec. 206. Effective date.\nTITLE III\u2014Other Administrative Reforms\nSec. 301. Petition for certiorari.\nSec. 302. Judicial review of actions related to campaign finance laws.\nSec. 303. Effective date.\nTITLE IV\u2014Stand by every ad\nSec. 401. Short title.\nSec. 402. Stand by every ad.\nSec. 403. Disclaimer requirements for communications made through prerecorded telephone calls.\nSec. 404. No expansion of persons subject to disclaimer requirements on internet communications.\nSec. 405. Effective date.\nTITLE V\u2014Severability\nSec. 501. Severability.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCampaign finance disclosure is a narrowly tailored and minimally restrictive means to advance substantial government interests, including fostering an informed electorate capable of engaging in self-government and holding their elected officials accountable, detecting and deterring quid pro quo corruption, and identifying information necessary to enforce other campaign finance laws, including campaign contribution limits and the prohibition on foreign money in U.S. campaigns. To further these substantial interests, campaign finance disclosure must be timely and complete, and must disclose the true and original source of money given, transferred, and spent to influence Federal elections. Current law does not meet this objective because corporations and other entities that the Supreme Court has permitted to spend money to influence Federal elections are subject to few if any transparency requirements.\n**(2)**\nAs the Supreme Court recognized in its per curiam opinion in Buckley v. Valeo, 424 U.S. 1, (1976), disclosure requirements certainly in most applications appear to be the least restrictive means of curbing the evils of campaign ignorance and corruption that Congress found to exist. Buckley, 424 U.S. at 68. In Citizens United v. FEC, the Court reiterated that disclosure is a less restrictive alternative to more comprehensive regulations of speech. 558 U.S. 310, 369 (2010).\n**(3)**\nNo subsequent decision has called these holdings into question, including the Court\u2019s decision in Americans for Prosperity Foundation v. Bonta, 141 S. Ct. 2373 (2021). That case did not involve campaign finance disclosure, and the Court did not overturn its longstanding recognition of the substantial interests furthered by such disclosure.\n**(4)**\nCampaign finance disclosure is also essential to enforce the Federal Election Campaign Act\u2019s prohibition on contributions by and solicitations of foreign nationals. See section 319 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121).\n**(5)**\nCongress should close loopholes allowing spending by foreign nationals in domestic elections. For example, in 2021, the Federal Election Commission, the independent Federal agency charged with protecting the integrity of the Federal campaign finance process, found reason to believe and conciliated a matter where an experienced political consultant knowingly and willfully violated Federal law by soliciting a contribution from a foreign national by offering to transmit a $2,000,000 contribution to a super PAC through his company and two 501(c)(4) organizations, to conceal the origin of the funds. This scheme was only unveiled after appearing in a The Telegraph UK article and video capturing the solicitation. See Conciliation Agreement, MURs 7165 & 7196 (Great America PAC, et al.), date June 28, 2021; Factual and Legal Analysis, MURs 7165 & 7196 (Jesse Benton), dated Mar. 2, 2021.\nI\nClosing Loopholes Allowing Spending by Foreign Nationals in Elections\n#### 101. Clarification of application of foreign money ban to certain disbursements and activities\nSection 319(b) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121(b)) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and by moving such subparagraphs 2 ems to the right;\n**(2)**\nby striking As used in this section, the term and inserting the following:\nDefinitions .\u2014For purposes of this section\u2014 (1) Foreign national The term ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Contribution and donation For purposes of paragraphs (1) and (2) of subsection (a), the term contribution or donation includes any disbursement to a political committee which accepts donations or contributions that do not comply with any of the limitations, prohibitions, and reporting requirements of this Act (or any disbursement to or on behalf of any account of a political committee which is established for the purpose of accepting such donations or contributions), or to any other person for the purpose of funding an expenditure, independent expenditure, or electioneering communication (as defined in section 304(f)(3)). .\n#### 102. Study and report on illicit foreign money in Federal elections\n##### (a) Study\nFor each 4-year election cycle (beginning with the 4-year election cycle ending in 2024), the Comptroller General shall conduct a study on the incidence of illicit foreign money in all elections for Federal office held during the preceding 4-year election cycle, including what information is known about the presence of such money in elections for Federal office.\n##### (b) Report\n**(1) In general**\nNot later than the applicable date with respect to any 4-year election cycle, the Comptroller General shall submit to the appropriate congressional committees a report on the study conducted under subsection (a).\n**(2) Matters included**\nThe report submitted under paragraph (1) shall include a description of the extent to which illicit foreign money was used to target particular groups, including rural communities, African-American and other minority communities, and military and veteran communities, based on such targeting information as is available and accessible to the Comptroller General.\n**(3) Applicable date**\nFor purposes of paragraph (1), the term applicable date means\u2014\n**(A)**\nin the case of the 4-year election cycle ending in 2024, the date that is 1 year after the date of the enactment of this Act; and\n**(B)**\nin the case of any other 4-year election cycle, the date that is 1 year after the date on which such 4-year election cycle ends.\n##### (c) Definitions\nAs used in this section:\n**(1) 4-year election cycle**\nThe term 4-year election cycle means the 4-year period ending on the date of the general election for the offices of President and Vice President.\n**(2) Illicit foreign money**\nThe term illicit foreign money means any contribution, donation, expenditure, or disbursement by a foreign national (as defined in section 319(b) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121(b))) prohibited under such section.\n**(3) Election; Federal office**\nThe terms election and Federal office have the meanings given such terms under section 301 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30101).\n**(4) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on House Administration of the House of Representatives;\n**(B)**\nthe Committee on Rules and Administration of the Senate;\n**(C)**\nthe Committee on the Judiciary of the House of Representatives; and\n**(D)**\nthe Committee on the Judiciary of the Senate.\n##### (d) Sunset\nThis section shall not apply to any 4-year election cycle beginning after the election for the offices of President and Vice President in 2036.\n#### 103. Prohibition on contributions and donations by foreign nationals in connection with ballot initiatives and referenda\n##### (a) In general\nSection 319(b) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121(b)), as amended by section 101, is amended by adding at the end the following new paragraphs:\n(3) Federal, State, or local election The term Federal, State, or local election includes a State or local ballot initiative or referendum, but only in the case of\u2014 (A) a covered foreign national as defined in paragraph (4); or (B) a foreign principal described in section 1(b)(2) or 1(b)(3) of the Foreign Agent Registration Act of 1938, as amended (22 U.S.C. 611(b)(2), (b)(3)) or an agent of such a foreign principal under such Act. (4) Covered foreign national (A) In general The term covered foreign national means\u2014 (i) a foreign principal (as defined in section 1(b) of the Foreign Agents Registration Act of 1938 (22 U.S.C. 611(b))) that is a government of a foreign country or a foreign political party; (ii) any person who acts as an agent, representative, employee, or servant, or any person who acts in any other capacity at the order, request, or under the direction or control, of a foreign principal described in clause (i) or of a person any of whose activities are directly or indirectly supervised, directed, controlled, financed, or subsidized in whole or in major part by a foreign principal described in clause (i); or (iii) any person included in the list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury pursuant to authorities relating to the imposition of sanctions relating to the conduct of a foreign principal described in clause (i). (B) Clarification regarding application to citizens of the United States In the case of a citizen of the United States, clause (ii) of subparagraph (A) applies only to the extent that the person involved acts within the scope of that person\u2019s status as the agent of a foreign principal described in clause (i) of subparagraph (A). .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to elections held in 2026 or any succeeding year.\n#### 104. Disbursements and activities subject to foreign money ban\n##### (a) Disbursements described\nSection 319(a)(1) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121(a)(1)) is amended\u2014\n**(1)**\nby striking or at the end of subparagraph (B); and\n**(2)**\nby striking subparagraph (C) and inserting the following:\n(C) an expenditure; (D) an independent expenditure; (E) a disbursement for an electioneering communication (within the meaning of section 304(f)(3)); (F) a disbursement for a communication which is placed or promoted for a fee on a website, web application, or digital application that refers to a clearly identified candidate for election for Federal office and is disseminated within 60 days before a general, special or runoff election for the office sought by the candidate or 30 days before a primary or preference election, or a convention or caucus of a political party that has authority to nominate a candidate for the office sought by the candidate; (G) a disbursement by a covered foreign national (as defined in subsection (b)(4)) for a broadcast, cable or satellite communication, or for a communication which is placed or promoted for a fee on a website, web application, or digital application, that promotes, supports, attacks, or opposes the election of a clearly identified candidate for Federal, State, or local office (regardless of whether the communication contains express advocacy or the functional equivalent of express advocacy); (H) a disbursement for a broadcast, cable, or satellite communication, or for any communication which is placed or promoted for a fee on an online platform (as defined in subsection (b)(5)), that discusses a national legislative issue of public importance in a year in which a regularly scheduled general election for Federal office is held, but only if the disbursement is made by a covered foreign national (as defined in subsection (b)(4)); (I) a disbursement by a covered foreign national (as defined in subsection (b)(4)) to compensate any person for internet activity that promotes, supports, attacks or opposes the election of a clearly identified candidate for Federal, State, or local office (regardless of whether the activity contains express advocacy or the functional equivalent of express advocacy); or (J) a disbursement by a covered foreign national (as defined in subsection (b)(4)) for a Federal judicial nomination communication (as defined in section 324(g)(2)); .\n##### (b) Definition of online platform\nSection 319(b) of such Act (52 U.S.C. 30121(b)), as amended by sections 101 and 103, is amended by adding at the end the following new paragraph:\n(5) Online platform (A) In general For purposes of this section, subject to subparagraph (B), the term online platform means any public-facing website, web application, or digital application (including a social network, ad network, or search engine) which\u2014 (i) (I) sells qualified political advertisements; and (II) has 50,000,000 or more unique monthly United States visitors or users for a majority of months during the preceding 12 months; or (ii) is a third-party advertising vendor that has 50,000,000 or more unique monthly United States visitors in the aggregate on any advertisement space that it has sold or bought for a majority of months during the preceding 12 months, as measured by an independent digital ratings service accredited by the Media Ratings Council (or its successor). (B) Exemption Such term shall not include any online platform that is a distribution facility of any broadcasting station or newspaper, magazine, blog, publication, or periodical. (C) Third-party advertising vendor defined For purposes of this subsection, the term third-party advertising vendor includes, but is not limited to, any third-party advertising vendor network, advertising agency, advertiser, or third-party advertisement serving company that buys and sells advertisement space on behalf of unaffiliated third-party websites, search engines, digital applications, or social media sites. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to disbursements made on or after the date of the enactment of this Act.\n#### 105. Prohibiting establishment of corporation to conceal election contributions and donations by foreign nationals\n##### (a) Prohibition\nChapter 29 of title 18, United States Code is amended by adding at the end the following:\n612. Establishment of corporation to conceal election contributions and donations by foreign nationals (a) Offense It shall be unlawful for an owner, officer, attorney, or incorporation agent of a corporation, company, or other entity to establish or use the corporation, company, or other entity with the intent to conceal an activity of a foreign national (as defined in section 319 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121)) prohibited under such section 319. (b) Penalty Any person who violates subsection (a) shall be imprisoned for not more than 5 years, fined under this title, or both. .\n##### (b) Table of sections\nThe table of sections for chapter 29 of title 18, United States Code is amended by adding at the end the following new item:\n612. Establishment of corporation to conceal election contributions and donations by foreign nationals. .\nII\nReporting of Campaign-Related Disbursements\n#### 201. Reporting of campaign-related disbursements\n##### (a) In general\nSection 324 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30126) is amended to read as follows:\n324. Disclosure of campaign-related disbursements by covered organizations (a) Disclosure statement (1) In general Any covered organization that makes campaign-related disbursements aggregating more than $10,000 in an election reporting cycle shall, not later than 24 hours after each disclosure date, file a statement with the Commission made under penalty of perjury that contains the information described in paragraph (2)\u2014 (A) in the case of the first statement filed under this subsection, for the period beginning on the first day of the election reporting cycle (or, if earlier, the period beginning one year before the first such disclosure date) and ending on the first such disclosure date; and (B) in the case of any subsequent statement filed under this subsection, for the period beginning on the previous disclosure date and ending on such disclosure date. (2) Information described The information described in this paragraph is as follows: (A) The name of the covered organization and the principal place of business of such organization and, in the case of a covered organization that is a corporation (other than a business concern that is an issuer of a class of securities registered under section 12 of the Securities Exchange Act of 1934 (15 U.S.C. 78l) or that is required to file reports under section 15(d) of that Act (15 U.S.C. 78o(d))) or an entity described in subsection (e)(2), a list of the beneficial owners (as defined in paragraph (4)(A)) of the entity that\u2014 (i) identifies each beneficial owner by name and current residential or business street address; and (ii) if any beneficial owner exercises control over the entity through another legal entity, such as a corporation, partnership, limited liability company, or trust, identifies each such other legal entity and each such beneficial owner who will use that other entity to exercise control over the entity. (B) The amount of each campaign-related disbursement made by such organization during the period covered by the statement of more than $1,000, and the name and address of the person to whom the disbursement was made. (C) In the case of a campaign-related disbursement that is not a covered transfer, the election to which the campaign-related disbursement pertains and if the disbursement is made for a public communication, the name of any candidate identified in such communication and if such communication is in support of or in opposition to the identified candidate. (D) A certification by the chief executive officer or person who is the head of the covered organization that the campaign-related disbursement is not made in cooperation, consultation, or concert with or at the request or suggestion of a candidate, authorized committee, or agent of a candidate, political party, or agent of a political party. (E) (i) If the covered organization makes campaign-related disbursements using exclusively funds in a campaign-related disbursement segregated fund, for each payment made to the account by a person other than the covered organization\u2014 (I) the name and address of each person who made such payment to the account during the period covered by the statement; (II) the date and amount of such payment; and (III) the aggregate amount of all such payments made by the person during the period beginning on the first day of the election reporting cycle (or, if earlier, the period beginning one year before the disclosure date) and ending on the disclosure date, but only if such payment was made by a person who made payments to the account in an aggregate amount of $10,000 or more during the period beginning on the first day of the election reporting cycle (or, if earlier, the period beginning one year before the disclosure date) and ending on the disclosure date. (ii) In any calendar year after 2027, section 315(c)(1)(B) shall apply to the amount described in clause (i) in the same manner as such section applies to the limitations established under subsections (a)(1)(A), (a)(1)(B), (a)(3), and (h) of such section, except that for purposes of applying such section to the amounts described in subsection (b), the base period shall be calendar year 2027. (F) (i) If the covered organization makes campaign-related disbursements using funds other than funds in a campaign-related disbursement segregated fund, for each payment to the covered organization\u2014 (I) the name and address of each person who made such payment during the period covered by the statement; (II) the date and amount of such payment; and (III) the aggregate amount of all such payments made by the person during the period beginning on the first day of the election reporting cycle (or, if earlier, the period beginning one year before the disclosure date) and ending on the disclosure date, but only if such payment was made by a person who made payments to the covered organization in an aggregate amount of $10,000 or more during the period beginning on the first day of the election reporting cycle (or, if earlier, the period beginning one year before the disclosure date) and ending on the disclosure date. (ii) In any calendar year after 2027, section 315(c)(1)(B) shall apply to the amount described in clause (i) in the same manner as such section applies to the limitations established under subsections (a)(1)(A), (a)(1)(B), (a)(3), and (h) of such section, except that for purposes of applying such section to the amounts described in subsection (b), the base period shall be calendar year 2027. (G) Such other information as required in rules established by the Commission to promote the purposes of this section. (3) Exceptions (A) Amounts received in ordinary course of business The requirement to include in a statement filed under paragraph (1) the information described in paragraph (2) shall not apply to amounts received by the covered organization in commercial transactions in the ordinary course of any trade or business conducted by the covered organization or in the form of investments (other than investments by the principal shareholder in a limited liability corporation) in the covered organization. For purposes of this subparagraph, amounts received by a covered organization as remittances from an employee to the employee\u2019s collective bargaining representative shall be treated as amounts received in commercial transactions in the ordinary course of the business conducted by the covered organization. (B) Donor restriction on use of funds The requirement to include in a statement submitted under paragraph (1) the information described in subparagraph (F) of paragraph (2) shall not apply if\u2014 (i) the person described in such subparagraph prohibited, in writing, the use of the payment made by such person for campaign-related disbursements; and (ii) the covered organization followed the prohibition and deposited the payment in an account which is segregated from a campaign-related disbursement segregated fund and any other account used to make campaign-related disbursements. (C) Threat of harassment or reprisal The requirement to include any information relating to the name or address of any person (other than a candidate) in a statement submitted under paragraph (1) shall not apply to any person or persons who provide specific and particular evidence establishing that the inclusion of such information would subject that person or persons to serious threats, harassment, or reprisals. For purposes of the preceding sentence, the terms threats , harassment , and reprisals do not include social ostracism, negative commentary, or criticism. (4) Other definitions For purposes of this section: (A) Beneficial owner defined (i) In general Except as provided in clause (ii), the term beneficial owner means, with respect to any entity, a natural person who, directly or indirectly\u2014 (I) exercises substantial control over an entity through ownership, voting rights, agreement, or otherwise; or (II) has a substantial interest in, or receives substantial economic benefits from, the assets of an entity. (ii) Exceptions The term beneficial owner shall not include\u2014 (I) a minor child; (II) a person acting as a nominee, intermediary, custodian, or agent on behalf of another person; (III) a person acting solely as an employee of an entity and whose control over, or economic benefits from, the entity derives solely from the employment status of the person; (IV) a person whose only interest in an entity is through a right of inheritance, unless the person also meets the requirements of clause (i); or (V) a creditor of an entity, unless the creditor also meets the requirements of clause (i). (iii) Anti-abuse rule The exceptions under clause (ii) shall not apply if used for the purpose of evading, circumventing, or abusing the provisions of clause (i) or paragraph (2)(A). (B) Campaign-related disbursement segregated fund The term campaign-related disbursement segregated fund means a segregated bank account consisting of funds that were paid directly to such account by persons other than the covered organization that controls the account. (C) Disclosure date The term disclosure date means\u2014 (i) the first date during any election reporting cycle by which a person has made campaign-related disbursements aggregating more than $10,000; and (ii) any other date during such election reporting cycle by which a person has made campaign-related disbursements aggregating more than $10,000 since the most recent disclosure date for such election reporting cycle. (D) Election reporting cycle The term election reporting cycle means the 2-year period beginning on the date of the most recent general election for Federal office. (E) Payment The term payment includes any contribution, donation, transfer, payment of dues, or other payment. (b) Coordination with other provisions (1) Other reports filed with the Commission Information included in a statement filed under this section may be excluded from statements and reports filed under section 304. (2) Treatment as separate segregated fund A campaign-related disbursement segregated fund may be treated as a separate segregated fund for purposes of section 527(f)(3) of the Internal Revenue Code of 1986. (c) Filing Statements required to be filed under subsection (a) shall be subject to the requirements of section 304(d) to the same extent and in the same manner as if such reports had been required under subsection (c) or (g) of section 304. (d) Campaign-Related disbursement defined (1) In general In this section, the term campaign-related disbursement means a disbursement by a covered organization for any of the following: (A) An independent expenditure which expressly advocates the election or defeat of a clearly identified candidate for election for Federal office, or is the functional equivalent of express advocacy because, when taken as a whole, it can be interpreted by a reasonable person only as advocating the election or defeat of a candidate for election for Federal office. (B) An applicable public communication. (C) An electioneering communication, as defined in section 304(f)(3). (D) A covered transfer. (2) Applicable public communications (A) In general The term applicable public communication means any public communication, including any communication that is produced for a fee or is placed or promoted for a fee on a website or digital device, application, service, or platform, that refers to a clearly identified candidate for election for Federal office and which promotes or supports the election of a candidate for that office, or attacks or opposes the election of a candidate for that office, without regard to whether the communication expressly advocates a vote for or against a candidate for that office. (B) Exception Such term shall not include any news story, commentary, or editorial distributed through the facilities of any broadcasting station or any print, online, or digital newspaper, magazine, publication, or periodical, unless such facilities are owned or controlled by any political party, political committee, or candidate. (e) Covered organization defined In this section, the term covered organization means any of the following: (1) A corporation (other than an organization described in section 501(c)(3) of the Internal Revenue Code of 1986). (2) A limited liability corporation that is not otherwise treated as a corporation for purposes of this Act (other than an organization described in section 501(c)(3) of the Internal Revenue Code of 1986). (3) An organization described in section 501(c) of such Code and exempt from taxation under section 501(a) of such Code (other than an organization described in section 501(c)(3) of such Code). (4) A labor organization (as defined in section 316(b)). (5) Any political organization under section 527 of the Internal Revenue Code of 1986, other than a political committee under this Act (except as provided in paragraph (6)). (6) A political committee with an account that accepts donations or contributions that do not comply with the contribution limits or source prohibitions under this Act, but only with respect to such accounts. (f) Covered transfer defined (1) In general In this section, the term covered transfer means any transfer or payment of funds by a covered organization to another person if the covered organization\u2014 (A) designates, requests, or suggests that the amounts be used for\u2014 (i) campaign-related disbursements (other than covered transfers); or (ii) making a transfer to another person for the purpose of making or paying for such campaign-related disbursements; (B) made such transfer or payment in response to a solicitation or other request for a donation or payment for\u2014 (i) the making of or paying for campaign-related disbursements (other than covered transfers); or (ii) making a transfer to another person for the purpose of making or paying for such campaign-related disbursements; (C) engaged in discussions with the recipient of the transfer or payment regarding\u2014 (i) the making of or paying for campaign-related disbursements (other than covered transfers); or (ii) donating or transferring any amount of such transfer or payment to another person for the purpose of making or paying for such campaign-related disbursements; or (D) knew or had reason to know that the person receiving the transfer or payment would make campaign-related disbursements in an aggregate amount of $50,000 or more during the 2-year period beginning on the date of the transfer or payment. (2) Exclusions The term covered transfer does not include any of the following: (A) A disbursement made by a covered organization in a commercial transaction in the ordinary course of any trade or business conducted by the covered organization or in the form of investments made by the covered organization. (B) A disbursement made by a covered organization if\u2014 (i) the covered organization prohibited, in writing, the use of such disbursement for campaign-related disbursements; and (ii) the recipient of the disbursement followed the prohibition and deposited the disbursement in an account which is segregated from a campaign-related disbursement segregated fund and any other account used to make campaign-related disbursements. (3) Special rule regarding transfers among affiliates (A) Special rule A transfer of an amount by one covered organization to another covered organization which is treated as a transfer between affiliates under subparagraph (C) shall be considered a covered transfer by the covered organization which transfers the amount only if the aggregate amount transferred during the year by such covered organization to that same covered organization is equal to or greater than $50,000. (B) Determination of amount of certain payments among affiliates In determining the amount of a transfer between affiliates for purposes of subparagraph (A), to the extent that the transfer consists of funds attributable to dues, fees, or assessments which are paid by individuals on a regular, periodic basis in accordance with a per-individual calculation which is made on a regular basis, the transfer shall be attributed to the individuals paying the dues, fees, or assessments and shall not be attributed to the covered organization. (C) Description of transfers between affiliates A transfer of amounts from one covered organization to another covered organization shall be treated as a transfer between affiliates if\u2014 (i) one of the organizations is an affiliate of the other organization; or (ii) each of the organizations is an affiliate of the same organization, except that the transfer shall not be treated as a transfer between affiliates if one of the organizations is established for the purpose of making campaign-related disbursements. (D) Determination of affiliate status For purposes of subparagraph (C), a covered organization is an affiliate of another covered organization if\u2014 (i) the governing instrument of the organization requires it to be bound by decisions of the other organization; (ii) the governing board of the organization includes persons who are specifically designated representatives of the other organization or are members of the governing board, officers, or paid executive staff members of the other organization, or whose service on the governing board is contingent upon the approval of the other organization; or (iii) the organization is chartered by the other organization. (E) Coverage of transfers to affiliated section 501(c)(3) organizations This paragraph shall apply with respect to an amount transferred by a covered organization to an organization described in paragraph (3) of section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code in the same manner as this paragraph applies to an amount transferred by a covered organization to another covered organization. (g) No effect on other reporting requirements Except as provided in subsection (b)(1), nothing in this section shall be construed to waive or otherwise affect any other requirement of this Act which relates to the reporting of campaign-related disbursements. .\n##### (b) Conforming amendment\nSection 304(f)(6) of such Act (52 U.S.C. 30104) is amended by striking Any requirement and inserting Except as provided in section 324(b), any requirement .\n##### (c) Regulations\nNot later than 6 months after the date of the enactment of this Act, the Federal Election Commission shall promulgate regulations relating to the application of the exemption under section 324(a)(3)(C) of the Federal Election Campaign Act of 1971 (as added by subsection (a)). Such regulations\u2014\n**(1)**\nshall require that the legal burden of establishing eligibility for such exemption is upon the organization required to make the report required under section 324(a)(1) of such Act (as added by subsection (a));\n**(2)**\nshall require reapplication for such exemption every 4 years;\n**(3)**\nshall provide that applications for such exemption, and documents reflecting the Federal Election Commission\u2019s consideration thereof, with appropriate redactions necessary to protect the personal information of any person or persons to whom such exemption applies, be published or made available for public inspection; and\n**(4)**\nshall be consistent with the principles applied in Citizens United v. Federal Election Commission, 558 U.S. 310 (2010).\n#### 202. Reporting of Federal judicial nomination disbursements\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nA fair and impartial judiciary is critical for our democracy and crucial to maintain the faith of the people of the United States in the justice system. As the Supreme Court held in Caperton v. Massey, there is a serious risk of actual bias\u2014based on objective and reasonable perceptions\u2014when a person with a personal stake in a particular case had a significant and disproportionate influence in placing the judge on the case. (Caperton v. A.T. Massey Coal Co., 556 U.S. 868, 884 (2009)).\n**(2)**\nPublic trust in government is at a historic low. According to polling, most Americans believe that corporations have too much power and influence in politics and the courts.\n**(3)**\nThe prevalence and pervasiveness of dark money drives public concern about corruption in politics and the courts. Dark money is funding for organizations and political activities that cannot be traced to actual donors. It is made possible by loopholes in our tax laws and regulations, weak oversight by the Internal Revenue Service, and donor-friendly court decisions.\n**(4)**\nUnder current law, social welfare organizations and business leagues can use funds to influence elections so long as political activity is not their primary activity. Super PACs can accept and spend unlimited contributions from any non-foreign source. These groups can spend tens of millions of dollars on political activities. Such dark money groups spent an estimated $1,050,000,000 in the 2020 election cycle.\n**(5)**\nDark money is used to shape judicial decision making. This can take many forms, akin to agency capture: influencing judicial selection by controlling who gets nominated and funding candidate advertisements; creating public relations campaigns aimed at mobilizing the judiciary around particular issues; and drafting law review articles, amicus briefs, and other products which tell judges how to decide a given case and provide ready-made arguments for willing judges to adopt.\n**(6)**\nOver the past decade, nonprofit organizations that do not disclose their donors have spent hundreds of millions of dollars to influence the nomination and confirmation process for Federal judges. One organization alone has spent nearly $40,000,000 on advertisements supporting or opposing Supreme Court nominees since 2016.\n**(7)**\nAnonymous money spent on judicial nominations is not subject to any disclosure requirements. Federal election laws only regulate contributions and expenditures relating to electoral politics; thus, expenditures, contributions, and advocacy efforts for Federal judgeships are not covered under the Federal Election Campaign Act of 1971. Without more disclosure, the public has no way of knowing whether the people spending money supporting or opposing judicial nominations have business before the courts.\n**(8)**\nCongress and the American people have a compelling interest in knowing who is funding these campaigns to select and confirm judges to lifetime appointments on the Federal bench.\n##### (b) Reporting\nSection 324 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30126), as amended by section 201, is amended by redesignating subsection (g) as subsection (h) and by inserting after subsection (f) the following new subsection:\n(g) Application to Federal judicial nominations (1) In general For purposes of this section\u2014 (A) a disbursement by a covered organization for a Federal judicial nomination communication shall be treated as a campaign-related disbursement; and (B) in the case of campaign-related disbursements which are for Federal judicial nomination communications\u2014 (i) the dollar amounts in paragraphs (1) and (2) of subsection (a) shall be applied separately with respect to such disbursements and other campaign-related disbursements; (ii) the election reporting cycle shall be the calendar year in which the disbursement for the Federal judicial nomination communication is made; (iii) references to a candidate in subsections (a)(2)(C), (a)(2)(D), and (a)(3)(C) shall be treated as references to a nominee for a Federal judge or justice; (iv) the reference to an election in subsection (a)(2)(C) shall be treated as a reference to the nomination of such nominee. (2) Federal judicial nomination communication (A) In general The term Federal judicial nomination communication means any communication\u2014 (i) that is by means of any broadcast, cable, or satellite, paid internet, or paid digital communication, paid promotion, newspaper, magazine, outdoor advertising facility, mass mailing, telephone bank, telephone messaging effort of more than 500 substantially similar calls or electronic messages within a 30-day period, or any other form of general public political advertising; and (ii) which promotes, supports, attacks, or opposes the nomination or Senate confirmation of an individual as a Federal judge or justice. (B) Exception Such term shall not include any news story, commentary, or editorial distributed through the facilities of any broadcasting station or any print, online, or digital newspaper, magazine, publication, or periodical, unless such facilities are owned or controlled by any political party, political committee, or candidate. (C) Intent not required A disbursement for an item described in subparagraph (A) shall be treated as a disbursement for a Federal judicial nomination communication regardless of the intent of the person making the disbursement. .\n#### 203. Coordination with FinCEN\n##### (a) In general\nThe Director of the Financial Crimes Enforcement Network of the Department of the Treasury shall provide the Federal Election Commission with such information as necessary to assist in administering and enforcing section 324 of the Federal Election Campaign Act of 1971, as amended by this title.\n##### (b) Report\nNot later than 6 months after the date of the enactment of this Act, the Chairman of the Federal Election Commission, in consultation with the Director of the Financial Crimes Enforcement Network of the Department of the Treasury, shall submit to Congress a report with recommendations for providing further legislative authority to assist in the administration and enforcement of such section 324.\n#### 204. Application of foreign money ban to disbursements for campaign-related disbursements consisting of covered transfers\nSection 319(b)(2) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30121(a)(1)(A)), as amended by section 101, is amended\u2014\n**(1)**\nby striking includes any disbursement and inserting\nincludes\u2014 (A) any disbursement ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) any disbursement, other than a disbursement described in section 324(a)(3)(A), to another person who made a campaign-related disbursement consisting of a covered transfer (as described in section 324) during the 2-year period ending on the date of the disbursement. .\n#### 205. Sense of Congress regarding implementation\nIt is the sense of Congress that the Federal Election Commission should simplify the process for filing any disclosure required under the provisions of, and amendments made by, this title in order to ensure that such process is as easy and accessible as possible.\n#### 206. Effective date\nThe amendments made by this title shall apply with respect to disbursements made on or after January 1, 2027, and shall take effect without regard to whether or not the Federal Election Commission has promulgated regulations to carry out such amendments.\nIII\nOther Administrative Reforms\n#### 301. Petition for certiorari\nSection 307(a)(6) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30107(a)(6)) is amended by inserting (including a proceeding before the Supreme Court on certiorari) after appeal .\n#### 302. Judicial review of actions related to campaign finance laws\n##### (a) In general\nTitle IV of the Federal Election Campaign Act of 1971 (52 U.S.C. 30141 et seq.) is amended by inserting after section 406 the following new section:\n407. Judicial review (a) In general If any action is brought for declaratory or injunctive relief to challenge, whether facially or as-applied, the constitutionality or lawfulness of any provision of this Act, including title V, or of chapter 95 or 96 of the Internal Revenue Code of 1986, or is brought to with respect to any action of the Commission under chapter 95 or 96 of the Internal Revenue Code of 1986, the following rules shall apply: (1) The action shall be filed in the United States District Court for the District of Columbia and an appeal from the decision of the district court may be taken to the Court of Appeals for the District of Columbia Circuit. (2) In the case of an action relating to declaratory or injunctive relief to challenge the constitutionality of a provision, the party filing the action shall concurrently deliver a copy of the complaint to the Clerk of the House of Representatives and the Secretary of the Senate. (3) It shall be the duty of the United States District Court for the District of Columbia and the Court of Appeals for the District of Columbia Circuit to advance on the docket and to expedite to the greatest possible extent the disposition of the action and appeal. (b) Clarifying scope of jurisdiction If an action at the time of its commencement is not subject to subsection (a), but an amendment, counterclaim, cross-claim, affirmative defense, or any other pleading or motion is filed challenging, whether facially or as-applied, the constitutionality or lawfulness of this Act or of chapter 95 or 96 of the Internal Revenue Code of 1986, or is brought to with respect to any action of the Commission under chapter 95 or 96 of the Internal Revenue Code of 1986, the district court shall transfer the action to the District Court for the District of Columbia, and the action shall thereafter be conducted pursuant to subsection (a). (c) Intervention by Members of Congress In any action described in subsection (a) relating to declaratory or injunctive relief to challenge the constitutionality of a provision, any Member of the House of Representatives (including a Delegate or Resident Commissioner to the Congress) or Senate shall have the right to intervene either in support of or opposition to the position of a party to the case regarding the constitutionality of the provision. To avoid duplication of efforts and reduce the burdens placed on the parties to the action, the court in any such action may make such orders as it considers necessary, including orders to require interveners taking similar positions to file joint papers or to be represented by a single attorney at oral argument. (d) Challenge by Members of Congress Any Member of Congress may bring an action, subject to the special rules described in subsection (a), for declaratory or injunctive relief to challenge, whether facially or as-applied, the constitutionality of any provision of this Act or chapter 95 or 96 of the Internal Revenue Code of 1986. .\n##### (b) Conforming amendments\n**(1)**\nSection 9011 of the Internal Revenue Code of 1986 is amended to read as follows:\n9011. Judicial review For provisions relating to judicial review of certifications, determinations, and actions by the Commission under this chapter, see section 407 of the Federal Election Campaign Act of 1971. .\n**(2)**\nSection 9041 of the Internal Revenue Code of 1986 is amended to read as follows:\n9041. Judicial review For provisions relating to judicial review of actions by the Commission under this chapter, see section 407 of the Federal Election Campaign Act of 1971. .\n**(3)**\nSection 310 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30110) is repealed.\n**(4)**\nSection 403 of the Bipartisan Campaign Reform Act of 2002 (52 U.S.C. 30110 note) is repealed.\n#### 303. Effective date\nThe amendments made by this title shall take effect and apply on the date of the enactment of this Act, without regard to whether or not the Federal Election Commission has promulgated regulations to carry out this title and the amendments made by this title.\nIV\nStand by every ad\n#### 401. Short title\nThis title may be cited as the Stand By Every Ad Act .\n#### 402. Stand by every ad\n##### (a) Expanded disclaimer requirements for certain communications\nSection 318 of the Federal Election Campaign Act of 1971 (52 U.S.C. 30120) is amended by adding at the end the following new subsection:\n(e) Expanded disclaimer requirements for communications not authorized by candidates or committees (1) In general Except as provided in paragraph (6), any communication described in paragraph (3) of subsection (a) which is transmitted in an audio or video format (including an internet or digital communication), or which is an internet or digital communication transmitted in a text or graphic format, shall include, in addition to the requirements of paragraph (3) of subsection (a), the following: (A) The individual disclosure statement described in paragraph (2)(A) (if the person paying for the communication is an individual) or the organizational disclosure statement described in paragraph (2)(B) (if the person paying for the communication is not an individual). (B) If the communication is transmitted in a video format, or is an internet or digital communication which is transmitted in a text or graphic format, and is paid for in whole or in part with a payment which is treated as a campaign-related disbursement under section 324\u2014 (i) the Top Five Funders list (if applicable); or (ii) in the case of a communication which, as determined on the basis of criteria established in regulations issued by the Commission, is of such short duration that including the Top Five Funders list in the communication would constitute a hardship to the person paying for the communication by requiring a disproportionate amount of the content of the communication to consist of the Top Five Funders list, the name of a website which contains the Top Five Funders list (if applicable) or, in the case of an internet or digital communication, an adapted disclaimer (as defined in paragraph (6)(C)) that directs persons reading, observing, or listening to the communication to the Top Five Funders list (if applicable). (C) If the communication is transmitted in an audio format and is paid for in whole or in part with a payment which is treated as a campaign-related disbursement under section 324\u2014 (i) the Top Two Funders list (if applicable); or (ii) in the case of a communication which, as determined on the basis of criteria established in regulations issued by the Commission, is of such short duration that including the Top Two Funders list in the communication would constitute a hardship to the person paying for the communication by requiring a disproportionate amount of the content of the communication to consist of the Top Two Funders list, the name of a website which contains the Top Two Funders list (if applicable). (2) Disclosure statements described (A) Individual disclosure statements The individual disclosure statement described in this subparagraph is the following: I am ________, and I approve this message. , with the blank filled in with the name of the applicable individual. (B) Organizational disclosure statements The organizational disclosure statement described in this subparagraph is the following: I am ________, the ________ of ________, and ________ approves this message. , with\u2014 (i) the first blank to be filled in with the name of the applicable individual; (ii) the second blank to be filled in with the title of the applicable individual; and (iii) the third and fourth blank each to be filled in with the name of the organization or other person paying for the communication. (3) Method of conveyance of statement (A) Communications in text or graphic format In the case of a communication to which this subsection applies which is transmitted in a text or graphic format, the disclosure statements required under paragraph (1) shall appear in letters at least as large as the majority of the text in the communication. (B) Communications transmitted in audio format In the case of a communication to which this subsection applies which is transmitted in an audio format, the disclosure statements required under paragraph (1) shall be made by audio by the applicable individual in a clear and conspicuous manner. (C) Communications transmitted in video format In the case of a communication to which this subsection applies which is transmitted in a video format, the information required under paragraph (1) shall appear in writing at the end of the communication or in a crawl along the bottom of the communication in a clear and conspicuous manner, with a reasonable degree of color contrast between the background and the printed statement, for a period of at least 6 seconds. (4) Applicable individual defined The term applicable individual means, with respect to a communication to which this subsection applies\u2014 (A) if the communication is paid for by an individual, the individual involved; (B) if the communication is paid for by a corporation, the chief executive officer of the corporation (or, if the corporation does not have a chief executive officer, the highest ranking official of the corporation); (C) if the communication is paid for by a labor organization, the highest ranking officer of the labor organization; and (D) if the communication is paid for by any other person, the highest ranking official of such person. (5) Top Five Funders list and Top Two Funders list defined (A) Top Five Funders list The term Top Five Funders list means, with respect to a communication which is paid for in whole or in part with a campaign-related disbursement (as defined in section 324), a list of the 5 persons who, during the 12-month period ending on the date of the disbursement, provided the largest payments of any type in an aggregate amount equal to or exceeding $10,000 to the person who is paying for the communication and the amount of the payments each such person provided. If 2 or more people provided the fifth largest of such payments, the person paying for the communication shall select 1 of those persons to be included on the Top Five Funders list. (B) Top two funders list The term Top Two Funders list means, with respect to a communication which is paid for in whole or in part with a campaign-related disbursement (as defined in section 324), a list of the persons who, during the 12-month period ending on the date of the disbursement, provided the largest and the second largest payments of any type in an aggregate amount equal to or exceeding $10,000 to the person who is paying for the communication and the amount of the payments each such person provided. If 2 or more persons provided the second largest of such payments, the person paying for the communication shall select 1 of those persons to be included on the Top Two Funders list. (C) Exclusion of certain payments For purposes of subparagraphs (A) and (B), in determining the amount of payments made by a person to a person paying for a communication, there shall be excluded the following: (i) Any amounts provided in the ordinary course of any trade or business conducted by the person paying for the communication or in the form of investments in the person paying for the communication. (ii) Any payment which the person prohibited, in writing, from being used for campaign-related disbursements, but only if the person paying for the communication followed the prohibition and deposited the payment in an account which is segregated from a campaign-related disbursement segregated fund (as defined in section 324) and any other account used to make campaign-related disbursements. (6) Special rules for certain communications (A) Exception for communications paid for by political parties and certain political committees This subsection does not apply to any communication to which subsection (d)(2) applies. (B) Treatment of video communications lasting 10 seconds or less In the case of a communication to which this subsection applies which is transmitted in a video format, or is an internet or digital communication which is transmitted in a text or graphic format, the communication shall meet the following requirements: (i) The communication shall include the individual disclosure statement described in paragraph (2)(A) (if the person paying for the communication is an individual) or the organizational disclosure statement described in paragraph (2)(B) (if the person paying for the communication is not an individual). (ii) The statement described in clause (i) shall appear in writing at the end of the communication, or in a crawl along the bottom of the communication, in a clear and conspicuous manner, with a reasonable degree of color contrast between the background and the printed statement, for a period of at least 4 seconds. (iii) To the extent that the format in which the communication is made permits the use of an adapted disclaimer, the communication shall include an adapted disclaimer that directs persons reading, observing, or listening to the communication to all of the information described in paragraph (1)(B)(i) of this subsection with respect to the communication. If the format will not allow for an adapted disclaimer, the communication shall include, in a clear and conspicuous manner, a website address with a landing page which will provide all of the information described in paragraph (1)(B)(i) of this subsection with respect to the communication. The adapted disclaimer or website address shall appear for the full duration of the communication. (C) Definitions In this subsection: (i) Adapted disclaimer The term adapted disclaimer means a statement that satisfies the requirements of paragraph (1)(B)(i) of this subsection and includes an indicator and a mechanism. (ii) Indicator The term indicator means any visible or audible element associated with a communication that is presented in a clear and conspicuous manner and gives notice to persons reading, observing, or listening to the communication that they may read, observe, or listen to a disclaimer satisfying the requirements of paragraph (1)(B)(i) of this subsection through a mechanism. An indicator may take any form, including words, images, sounds, symbols, and icons. (iii) Mechanism The term mechanism means any use of technology that enables the person reading, observing, or listening to a communication to read, observe, or listen to a disclaimer satisfying the requirements of paragraph (1)(B)(i) of this subsection after not more than 1 action by a recipient of the communication. A mechanism may take any form, including hover-over text, pop-up screens, scrolling text, rotating panels, and hyperlinks to a landing page. .\n##### (b) Application of expanded requirements to campaign-Related disbursements\n**(1) In general**\nSection 318(a) of such Act (52 U.S.C. 30120(a)) is amended by striking for the purpose of financing communications expressly advocating the election or defeat of a clearly identified candidate and inserting for a campaign-related disbursement described in subparagraph (A), (B), or (C) of section 324(d)(1) .\n**(2) Clarification of exemption from inclusion of candidate disclaimer statement in Federal judicial nomination communications**\nSection 318(a)(3) of such Act (52 U.S.C. 30120(a)(3)) is amended by striking shall clearly state and inserting shall (except in the case of a Federal judicial nomination communication, as defined in section 324(d)(3)) clearly state .\n##### (c) Exception for communications paid for by political parties and certain political committees\nSection 318(d)(2) of such Act (52 U.S.C. 30120(d)(2)) is amended\u2014\n**(1)**\nin the heading, by striking Others and inserting Certain political committees ;\n**(2)**\nby striking Any communication and inserting (A) Any communication ;\n**(3)**\nby inserting which (except to the extent provided in subparagraph (B)) is paid for by a political committee (including a political committee of a political party) and after subsection (a) ;\n**(4)**\nby striking or other person each place it appears; and\n**(5)**\nby adding at the end the following new subparagraph:\n(B) (i) This paragraph does not apply to a communication paid for in whole or in part during a calendar year with a campaign-related disbursement, but only if the covered organization making the campaign-related disbursement made campaign-related disbursements (as defined in section 324) aggregating more than $10,000 during such calendar year. (ii) For purposes of clause (i), in determining the amount of campaign-related disbursements made by a covered organization during a year, there shall be excluded the following: (I) Any amounts received by the covered organization in the ordinary course of any trade or business conducted by the covered organization or in the form of investments in the covered organization. (II) Any amounts received by the covered organization from a person who prohibited, in writing, the organization from using such amounts for campaign-related disbursements, but only if the covered organization followed the prohibition and deposited the amounts in an account which is segregated from a campaign-related disbursement segregated fund (as defined in section 324) and any other account used to make campaign-related disbursements. .\n##### (d) Modification of additional requirements for certain communications\nSection 318(d) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30120(d)) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nby striking which is transmitted through radio and inserting which is in an audio format ; and\n**(B)**\nby striking By radio in the heading and inserting Audio format ;\n**(2)**\nin paragraph (1)(B)\u2014\n**(A)**\nby striking which is transmitted through television and inserting which is in video format ; and\n**(B)**\nby striking By television in the heading and inserting Video format ; and\n**(3)**\nin paragraph (2)\u2014\n**(A)**\nby striking transmitted through radio or television and inserting made in audio or video format ; and\n**(B)**\nby striking through television in the second sentence and inserting in video format .\n#### 403. Disclaimer requirements for communications made through prerecorded telephone calls\n##### (a) Application of requirements\n**(1) In general**\nSection 318(a) of the Federal Election Campaign Act of 1971 (52 U.S.C. 30120(a)) is amended by striking mailing each place it appears and inserting mailing, telephone call consisting in substantial part of a prerecorded audio message .\n**(2) Application to communications subject to expanded disclaimer requirements**\nSection 318(e)(1) of such Act (52 U.S.C. 30120(e)(1)), as added by section 402(a), is amended in the matter preceding subparagraph (A) by striking which is transmitted in an audio or video format and inserting which is transmitted in an audio or video format or which consists of a telephone call consisting in substantial part of a prerecorded audio message .\n##### (b) Treatment as communication transmitted in audio format\n**(1) Communications by candidates or authorized persons**\nSection 318(d) of such Act (52 U.S.C. 30120(d)) is amended by adding at the end the following new paragraph:\n(3) Prerecorded telephone calls Any communication described in paragraph (1), (2), or (3) of subsection (a) (other than a communication which is subject to subsection (e)) which is a telephone call consisting in substantial part of a prerecorded audio message shall include, in addition to the requirements of such paragraph, the audio statement required under subparagraph (A) of paragraph (1) or the audio statement required under paragraph (2) (whichever is applicable), except that the statement shall be made at the beginning of the telephone call. .\n**(2) Communications subject to expanded disclaimer requirements**\nSection 318(e)(3) of such Act (52 U.S.C. 30120(e)(3)), as added by section 402(a), is amended by adding at the end the following new subparagraph:\n(D) Prerecorded telephone calls In the case of a communication to which this subsection applies which is a telephone call consisting in substantial part of a prerecorded audio message, the communication shall be considered to be transmitted in an audio format. .\n#### 404. No expansion of persons subject to disclaimer requirements on internet communications\nNothing in this title or the amendments made by this title may be construed to require any person who is not required under section 318 of the Federal Election Campaign Act of 1971 to include a disclaimer on communications made by the person through the internet to include any disclaimer on any such communications.\n#### 405. Effective date\nThe amendments made by this title shall apply with respect to communications made on or after January 1, 2027, and shall take effect without regard to whether or not the Federal Election Commission has promulgated regulations to carry out such amendments.\nV\nSeverability\n#### 501. Severability\nIf any provision of this Act or amendment made by this Act, or the application of a provision or amendment to any person or circumstance, is held to be unconstitutional, the remainder of this Act and amendments made by this Act, and the application of the provisions and amendment to any person or circumstance, shall not be affected by the holding.",
      "versionDate": "",
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
        "actionDate": "2026-03-04",
        "text": "Referred to the Committee on House Administration, and in addition to the Committees on Ways and Means, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7802",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DISCLOSE Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2816",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shell Company Abuse Act",
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
        "updateDate": "2026-03-20T15:11:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-04",
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
          "measure-id": "id119s3991",
          "measure-number": "3991",
          "measure-type": "s",
          "orig-publish-date": "2026-03-04",
          "originChamber": "SENATE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3991v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2026-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Democracy Is Strengthened by Casting Light On Spending in Elections Act of 2026 or the DISCLOSE Act of </strong><strong>2026</strong></p><p>This bill addresses campaign finance, including by expanding the prohibition on campaign spending by foreign nationals, requiring additional disclosures of campaign expenditures, and requiring additional disclosures regarding certain political advertisements.</p><p>Specifically, the bill expands existing foreign money prohibitions to include disbursements for paid web-based or digital communications and federal judicial nomination communications. It also prohibits foreign nationals from contributing to campaigns related to ballot initiatives and referenda.</p><p>The Government Accountability Office must, for each four-year election cycle, study and report on the incidence of illicit foreign money in federal elections.</p><p>Next, the bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national. A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p><p>Covered organizations (e.g., corporations, labor organizations, and political organizations) must, within 24 hours, file reports with the Federal Election Commission to disclose campaign expenditures of more than $10,000 during an election cycle.</p><p>The bill also requires organizations to provide additional disclosures regarding political advertisements, including the donors who contributed the most money to that organization in the last year.</p>"
        },
        "title": "DISCLOSE Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3991.xml",
    "summary": {
      "actionDate": "2026-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Democracy Is Strengthened by Casting Light On Spending in Elections Act of 2026 or the DISCLOSE Act of </strong><strong>2026</strong></p><p>This bill addresses campaign finance, including by expanding the prohibition on campaign spending by foreign nationals, requiring additional disclosures of campaign expenditures, and requiring additional disclosures regarding certain political advertisements.</p><p>Specifically, the bill expands existing foreign money prohibitions to include disbursements for paid web-based or digital communications and federal judicial nomination communications. It also prohibits foreign nationals from contributing to campaigns related to ballot initiatives and referenda.</p><p>The Government Accountability Office must, for each four-year election cycle, study and report on the incidence of illicit foreign money in federal elections.</p><p>Next, the bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national. A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p><p>Covered organizations (e.g., corporations, labor organizations, and political organizations) must, within 24 hours, file reports with the Federal Election Commission to disclose campaign expenditures of more than $10,000 during an election cycle.</p><p>The bill also requires organizations to provide additional disclosures regarding political advertisements, including the donors who contributed the most money to that organization in the last year.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s3991"
    },
    "title": "DISCLOSE Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Democracy Is Strengthened by Casting Light On Spending in Elections Act of 2026 or the DISCLOSE Act of </strong><strong>2026</strong></p><p>This bill addresses campaign finance, including by expanding the prohibition on campaign spending by foreign nationals, requiring additional disclosures of campaign expenditures, and requiring additional disclosures regarding certain political advertisements.</p><p>Specifically, the bill expands existing foreign money prohibitions to include disbursements for paid web-based or digital communications and federal judicial nomination communications. It also prohibits foreign nationals from contributing to campaigns related to ballot initiatives and referenda.</p><p>The Government Accountability Office must, for each four-year election cycle, study and report on the incidence of illicit foreign money in federal elections.</p><p>Next, the bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national. A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p><p>Covered organizations (e.g., corporations, labor organizations, and political organizations) must, within 24 hours, file reports with the Federal Election Commission to disclose campaign expenditures of more than $10,000 during an election cycle.</p><p>The bill also requires organizations to provide additional disclosures regarding political advertisements, including the donors who contributed the most money to that organization in the last year.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119s3991"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3991is.xml"
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
      "title": "DISCLOSE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DISCLOSE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Democracy Is Strengthened by Casting Light On Spending in Elections Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stand By Every Ad Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Election Campaign Act of 1971 to provide for additional disclosure requirements for corporations, labor organizations, Super PACs and other entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:51Z"
    }
  ]
}
```
