# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2588?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2588
- Title: Sustaining Our Democracy Act
- Congress: 119
- Bill type: S
- Bill number: 2588
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-04-07T12:59:03Z
- Update date including text: 2026-04-21T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2588",
    "number": "2588",
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
    "title": "Sustaining Our Democracy Act",
    "type": "S",
    "updateDate": "2026-04-07T12:59:03Z",
    "updateDateIncludingText": "2026-04-21T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:12:35Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-31",
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
      "sponsorshipDate": "2025-07-31",
      "state": "VA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-31",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NJ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2588is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2588\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Padilla (for himself, Ms. Klobuchar , Ms. Warren , Mr. Schiff , Mr. Blumenthal , Mr. Markey , Mr. King , Mr. Kaine , Mr. Sanders , Mr. Welch , Ms. Smith , Mr. Kim , Mr. Wyden , Mr. Booker , Ms. Hirono , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo establish a democracy advancement and innovation program, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Sustaining Our Democracy Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Payments and Allocations to States\nSec. 101. Democracy Advancement and Innovation Program.\nSec. 102. State plan.\nSec. 103. Prohibitions.\nSec. 104. Amount of State allocation.\nSec. 105. Procedures for disbursements of payments and allocations.\nSec. 106. Office of Democracy Advancement and Innovation.\nTITLE II\u2014State Election Assistance and Innovation Trust Fund\nSec. 201. State Election Assistance and Innovation Trust Fund.\nTITLE III\u2014General Provisions\nSec. 301. Definitions.\nSec. 302. Rule of construction regarding calculation of deadlines.\nSec. 303. Severability.\nI\nPayments and Allocations to States\n#### 101. Democracy Advancement and Innovation Program\n##### (a) Establishment\nThere is established a program to be known as the Democracy Advancement and Innovation Program under which the Director of the Office of Democracy Advancement and Innovation shall make allocations to each State for each fiscal year to carry out democracy promotion activities described in subsection (b).\n##### (b) Democracy promotion activities described\nThe democracy promotion activities described in this subsection are as follows:\n**(1)**\nActivities to promote innovation to improve efficiency and smooth functioning in the administration of elections for Federal office and to secure the infrastructure used in the administration of such elections, including making upgrades to voting equipment and voter registration systems, voter registration and nonpartisan voter outreach activities, securing voting locations, expanding polling places and the availability of early and mail voting, and promoting cybersecurity.\n**(2)**\nActivities to recruit, train, and retain nonpartisan election officials and poll workers and to protect election officials (both nonpartisan and those elected or appointed to their position) from threats against them in the course of their work administering Federal elections.\n**(3)**\nActivities to increase access to voting in elections for Federal office by underserved communities, individuals with disabilities, racial and language minority groups, individuals entitled to vote by absentee ballot under the Uniformed and Overseas Citizens Absentee Voting Act, and voters residing in Indian lands.\n##### (c) Permitting States To retain and reserve allocations for future use\nA State may retain and reserve an allocation received for a fiscal year to carry out democracy promotion activities in any subsequent fiscal year.\n##### (d) Requiring submission and approval of State plan\n**(1) In general**\nA State shall receive an allocation under the Program for a fiscal year if\u2014\n**(A)**\nnot later than 90 days before the first day of the fiscal year, the chief State election official of the State submits to the Director the State plan described in section 102; and\n**(B)**\nnot later than 45 days before the first day of the fiscal year, the Director, in consultation with the Election Assistance Commission as described in paragraph (3), determines that the State plan will enable the State to carry out democracy promotion activities and approves the plan.\n**(2) Submission and approval of revised plan**\nIf the Director does not approve the State plan as submitted by the State under paragraph (1) with respect to a fiscal year, the State shall receive a payment under the Program for the fiscal year if, at any time prior to the end of the fiscal year\u2014\n**(A)**\nthe chief State election official of the State submits a revised version of the State plan; and\n**(B)**\nthe Director, in consultation with the Election Assistance Commission as described in paragraph (3), determines that the revised version of the State plan will enable the State to carry out democracy promotion activities and approves the plan.\n**(3) Election Assistance Commission consultation**\nWith respect to a State plan submitted under paragraph (1) or a revised plan submitted under paragraph (2)\u2014\n**(A)**\nthe Director shall, prior to making a determination on approval of the plan, consult with the Election Assistance Commission; and\n**(B)**\nthe Election Assistance Commission shall submit to the Director a written assessment with respect to whether the proposed activities of the plan satisfy the requirements of this Act.\n**(4) Consultation with legislature**\nThe chief State election official of the State shall develop the State plan submitted under paragraph (1) and any revised plan submitted under paragraph (2) in consultation with the majority party and minority party leaders of each house of the State legislature.\n**(5) Rules for States that do not submit a State plan**\nIf a State fails to submit a State plan described in section 102 before the date required under paragraph (1)(A), under rules established by the Director\u2014\n**(A)**\nfor purposes of this title (other than section 104)\u2014\n**(i)**\neach political subdivision within the State shall be treated as a State for purposes of this title (other than section 104); and\n**(ii)**\nin applying this title to such political subdivision, any duties required of the chief State election official shall be undertaken by the executive official of such political subdivision charged with the administration of elections;\n**(B)**\nin applying this subsection to any political subdivision of the State\u2014\n**(i)**\nparagraph (1)(A) shall be applied by substituting the first day of the fiscal year for 90 days before the first day of the fiscal year ;\n**(ii)**\nparagraph (1)(B) shall be applied by substituting 30 days after the first day of the fiscal year for 45 days before the first day of the fiscal year ; and\n**(iii)**\nparagraph (4) shall not apply; and\n**(C)**\nthe amount of the allocation made to each such political subdivision under the Program shall be the sum of\u2014\n**(i)**\nan amount which bears the same proportion to the amount determined under section 104 with respect to the State in which the political subdivision is located as\u2014\n**(I)**\nthe population of the political subdivision; bears to\n**(II)**\nthe population of such State; plus\n**(ii)**\nan amount (not to exceed 100 percent of the amount determined with respect to the political subdivision under clause (i)) which bears the same proportion to the unsubscribed funds of the State as\u2014\n**(I)**\nthe population of the political subdivision; bears to\n**(II)**\nthe population of the number of political subdivisions within the State that submitted a plan under section 102 before the date required under paragraph (1)(A) (after application of subparagraph (B)).\nFor purposes of subparagraph (C)(ii), the unsubscribed funds of any State is the sum of the amounts described in subparagraph (C)(i) with respect to political subdivisions in the State which did not submit a plan under this subsection before the date required under paragraph (1)(A) (after application of subparagraph (B)).\n##### (e) State report on use of allocations\nNot later than 90 days after the last day of a fiscal year for which an allocation was made to the State under the Program, the chief State election official of the State shall submit a report to the Director describing how the State used the allocation, including a description of the democracy promotion activities the State carried out with the allocation.\n##### (f) Public availability of information\n**(1) Publicly available website**\nThe Director shall make available on a publicly accessible website the following:\n**(A)**\nState plans submitted under paragraph (1) of subsection (d) and revised plans submitted under paragraph (2) of subsection (d).\n**(B)**\nThe Director\u2019s notifications of determinations with respect to such plans under subsection (d).\n**(C)**\nReports submitted by States under subsection (e).\n**(2) Redaction**\nThe Director may redact information required to be made available under paragraph (1) if the information would be properly withheld from disclosure under section 552 of title 5, United States Code, or if the public disclosure of the information is otherwise prohibited by law.\n##### (g) Effective date\nThis section shall apply with respect to fiscal year 2026 and each succeeding fiscal year.\n#### 102. State plan\n##### (a) Contents\nA State plan under this section with respect to a State is a plan containing each of the following:\n**(1)**\nA description of the democracy promotion activities the State will carry out with the payment made under the Program.\n**(2)**\nA statement of whether or not the State intends to retain and reserve the payment for future democracy promotion activities.\n**(3)**\nA statement of how the State intends to distribute resources under the plan, including how the distribution of resources will address geographic and racial disparities within the State.\n**(4)**\nA description of how the State intends to allocate funds to carry out the proposed activities, which shall include the amount the State intends to allocate to each such activity, including (if applicable) a specific allocation for\u2014\n**(A)**\nactivities described in subsection 101(b)(1) (relating to election administration);\n**(B)**\nactivities described in section 101(b)(2) (relating to activities to recruit, train, retain, and protect election workers); and\n**(C)**\nactivities described in section 101(b)(3) (relating to activities to increase access to voting in elections for Federal office by certain communities).\n**(5)**\nA description of how funds allocated under paragraph (4) will be allocated to political subdivisions of the State.\n**(6)**\nA description of how the State will establish the fund described in subsection (b) for purposes of administering the democracy promotion activities which the State will carry out with the payment, including information on fund management.\n**(7)**\nA description of the State-based administrative complaint procedures established for purposes of section 103(a)(2).\n**(8)**\nA statement regarding whether the proposed activities to be funded are permitted under State law, or whether the official intends to seek legal authorization for such activities.\n##### (b) Requirements for fund\n**(1) Fund described**\nFor purposes of subsection (a)(6), a fund described in this subsection with respect to a State is a fund which is established in the treasury of the State government, which is used in accordance with paragraph (2), and which consists of the following amounts:\n**(A)**\nAmounts appropriated or otherwise made available by the State for carrying out the democracy promotion activities for which the payment is made to the State under the Program.\n**(B)**\nThe payment made to the State under the Program.\n**(C)**\nSuch other amounts as may be appropriated under law.\n**(D)**\nInterest earned on deposits of the fund.\n**(2) Use of fund**\nAmounts in the fund shall be used by the State exclusively to carry out democracy promotion activities for which the payment is made to the State under the Program.\n**(3) Treatment of States that require changes to state law**\nIn the case of a State that requires State legislation to establish the fund described in this subsection, the Director shall defer disbursement of the payment to such State under the Program until such time as legislation establishing the fund is enacted.\n#### 103. Prohibitions\n##### (a) Prohibited uses of payments\n**(1) In general**\nA State may not use a payment made under the Program to carry out\u2014\n**(A)**\nany activity described in paragraph (2); or\n**(B)**\nany other activity which has the purpose or effect of diminishing the ability of any eligible voter to participate in the electoral process.\n**(2) Prohibited activities**\nThe following are activities described in this paragraph:\n**(A)**\nActivities that intimidate, threaten, or coerce voters, poll workers, or election administrators.\n**(B)**\nThe restriction of the distribution of food or nonalcoholic beverages to voters while waiting at polling places (other than restrictions on distributions made on the basis of the electoral participation or political preference of the recipient).\n**(C)**\nThe removal of election administrators from their positions other than for negligence, neglect of duty, or malfeasance in office.\n**(D)**\nDefending against lawsuits alleging voter-suppression practices or proposed practices.\n**(E)**\nThe investigation of claims of voter fraud based on the mere invocation of interests in voter confidence or prevention of fraud.\n**(F)**\nThe performance of audits that\u2014\n**(i)**\nfail to meet best practices established by the Election Assistance Commission;\n**(ii)**\nfail to meet the requirements for record retention under title III of the Civil Rights Act of 1960 ( 52 U.S.C. 20701 et seq. ); or\n**(iii)**\notherwise jeopardize election records, voting equipment, electronic poll books, or election management systems (as defined under the voluntary guidance issued by the Election Assistance Commission under section 311 of the Help America Vote Act of 2002 ( 52 U.S.C. 21101 )).\n**(G)**\nThe removal of voters from voter rolls based on evidence that is not reliable.\n**(H)**\nActivities preventing individuals seeking to have their right to vote or register to vote restored.\n**(I)**\nThe purchase of voting machines that do not require the use of individual voter-verifiable paper ballots marked through the use of a nontabulating ballot marking device or system.\n##### (b) State-Based administrative complaint procedures\n**(1) Establishment**\nA State receiving a payment under the Program shall establish uniform and nondiscriminatory State-based administrative complaint procedures under which any person who believes that a violation of subsection (a) has occurred, is occurring, or is about to occur may file a complaint.\n**(2) Notification to Director**\nThe State shall transmit to the Director a description of each complaint filed under the procedures, together with\u2014\n**(A)**\nif the State provides a remedy with respect to the complaint, a description of the remedy; or\n**(B)**\nif the State dismisses the complaint, a statement of the reasons for the dismissal.\n**(3) Review by Director**\n**(A) Request for review**\nAny person who is dissatisfied with the final decision under a State-based administrative complaint procedure under this subsection may, not later than 60 days after the decision is made, file a request with the Director to review the decision.\n**(B) Action by Director**\nUpon receiving a request under subparagraph (A), the Director shall review the decision and, in accordance with such procedures as the Director may establish, including procedures to provide notice and an opportunity for a hearing, may uphold the decision or reverse the decision and provide an appropriate remedy.\n**(C) Public availability of material**\nThe Director shall make available on a publicly accessible website all material relating to a request for review and determination by the Director under this paragraph, except that the Director may redact material required to be made available under this subparagraph if the material would be properly withheld from disclosure under section 552 of title 5, United States Code, or if the public disclosure of the material is otherwise prohibited by law.\n**(4) Right to petition for review**\n**(A) In general**\nAny person aggrieved by an action of the Director under subparagraph (B) of paragraph (3) may file a petition with the United States District Court for the District of Columbia.\n**(B) Deadline to file petition**\nAny petition under this subparagraph shall be filed not later than 60 days after the date of the action taken by the Director under subparagraph (B) of paragraph (3).\n**(C) Standard of review**\nIn any proceeding under this paragraph, the court shall determine whether the action of the Director was arbitrary, capricious, an abuse of discretion, or otherwise not in accordance with law under section 706 of title 5, United States Code, and may direct the Office to conform with any such determination within 30 days.\n##### (c) Action by Attorney General for declaratory and injunctive relief\nThe Attorney General may bring a civil action against any State in an appropriate United States District Court for such declaratory and injunctive relief (including a temporary restraining order, a permanent or temporary injunction, or other order) as may be necessary to enforce subsection (a).\n#### 104. Amount of State allocation\n##### (a) State-Specific amount\nThe amount of the allocation made to a State under the Program for a fiscal year shall be equal to the product of\u2014\n**(1)**\nthe Congressional district allocation amount (determined under subsection (b)); and\n**(2)**\nthe number of Congressional districts in the State for the next regularly scheduled general election for Federal office held in the State.\n##### (b) Congressional district allocation amount\nFor purposes of subsection (a), the Congressional district allocation amount with respect to a fiscal year is equal to the quotient of\u2014\n**(1)**\nthe aggregate amount available for allocations to States under the Program for the fiscal year, as determined by the Director under subsection (c); divided by\n**(2)**\nthe total number of Congressional districts in all States.\n##### (c) Determination of aggregate amount available for allocations; notification to States\nNot later than 120 days before the first day of each fiscal year, the Director\u2014\n**(1)**\nshall determine and establish the aggregate amount available for allocations to States under the Program for the fiscal year, taking into account the anticipated balances of the Trust Fund (including any amounts appropriated pursuant to section 106(i)); and\n**(2)**\nshall notify each State of the amount of the State\u2019s allocation under the Program for the fiscal year.\nIn making the determination under paragraph (1), the Director shall consult with the Election Assistance Commission, but shall be solely responsible for making the final determinations under such paragraph.\n##### (d) Source of payments\nThe amounts used to make allocations and payments under the Program shall be derived solely from the Trust Fund.\n#### 105. Procedures for disbursements of payments and allocations\n##### (a) Allocation\nUpon approving the State plan under section 102, the Director shall direct the Secretary of the Treasury to allocate to the Election Assistance Commission the amount provided for activities under the plan.\n##### (b) Payment to State\nAs soon as practicable after receiving an allocation under subsection (a) with respect to a State, the Election Assistance Commission shall make payments to\u2014\n**(1)**\nlocal election administrators in the State with respect to amounts related to activities in the State plan carried out directly by such local election administrators; and\n**(2)**\nthe State with respect to any amount not described in paragraph (1).\n##### (c) Continuing availability of funds after appropriation\nA payment made to a State by the Election Assistance Commission under this section shall be available without fiscal year limitation.\n#### 106. Office of Democracy Advancement and Innovation\n##### (a) Establishment\nThere is established as an independent establishment in the executive branch the Office of Democracy Advancement and Innovation.\n##### (b) Director\n**(1) In general**\nThe Office shall be headed by a Director, who shall be appointed by the President with the advice and consent of the Senate.\n**(2) Term of service**\nThe Director shall serve for a term of 6 years and may be reappointed to an additional term, and may continue serving as Director until a replacement is appointed. A vacancy in the position of Director shall be filled in the same manner as the original appointment.\n**(3) Compensation**\nThe Director shall be paid at an annual rate of pay equal to the annual rate in effect for level II of the Executive Schedule.\n**(4) Removal**\nThe Director may be removed from office by the President. If the President removes the Director, the President shall communicate in writing the reasons for the removal to both Houses of Congress not later than 30 days beforehand. Nothing in this paragraph shall be construed to prohibit a personnel action otherwise authorized by law.\n##### (c) General counsel and other staff\n**(1) General counsel**\nThe Director shall appoint a General Counsel who shall be paid at an annual rate of pay equal to the annual rate in effect for level III of the Executive Schedule. In the event of a vacancy in the position of the Director, the General Counsel shall exercise all the responsibilities of the Director until such vacancy is filled.\n**(2) Senior staff**\nThe Director may appoint and fix the pay of staff designated as Senior staff, such as a Deputy Director, who may be paid at an annual rate of pay equal to the annual rate in effect for level IV of the Executive Schedule.\n**(3) Other staff**\nIn addition to the General Counsel and Senior staff, the Director may appoint and fix the pay of such other staff as the Director considers necessary to carry out the duties of the Office, except that no such staff may be compensated at an annual rate exceeding the daily equivalent of the annual rate of basic pay in effect for grade GS\u201315 of the General Schedule.\n##### (d) Duties\nThe duties of the Office are as follows:\n**(1) Administration of Program**\nThe Director shall administer the Program, in consultation with the Election Assistance Commission, including by holding quarterly meetings of representatives from such Commission.\n**(2) Oversight of Trust Fund**\nThe Director shall oversee the operation of the Trust Fund and monitor its balances, in consultation with the Election Assistance Commission and the Secretary of the Treasury. The Director may hold funds in reserve to cover the expenses of the Office and to preserve the solvency of the Trust Fund.\n**(3) Reports**\nNot later than 180 days after the date of the regularly scheduled general election for Federal office held in 2026 and each succeeding regularly scheduled general election for Federal office thereafter, the Director, in consultation with the Election Assistance Commission, shall submit to the Committee on House Administration of the House of Representatives and the Committee on Rules and Administration of the Senate a report on the activities carried out under the Program and the amounts deposited into and paid from the Trust Fund during the two most recent fiscal years.\n##### (e) Coverage under Inspector General Act of 1978 for conducting audits and investigations\n**(1) In general**\nSection 415(a)(1)(A) of title 5, United States Code, is amended by inserting the Office of Democracy Advancement and Innovation, after Election Assistance Commission, .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall take effect 180 days after the appointment of the Director.\n##### (f) Coverage under Hatch Act\nClause (i) of section 7323(b)(2)(B) of title 5, United States Code, is amended\u2014\n**(1)**\nby striking or at the end of subclause (XIII); and\n**(2)**\nby adding at the end the following new subclause:\n(XV) the Office of Democracy Advancement and Innovation; or .\n##### (g) Regulations\n**(1) In general**\nExcept as provided in paragraph (2), not later than 270 days after the date of enactment of this Act, the Director shall promulgate such rules and regulations as the Director considers necessary and appropriate to carry out the duties of the Office under this Act and the amendments made by this Act.\n**(2) State plan submission and approval and distribution of funds**\nNot later than 90 days after the date of the enactment of this Act, the Director shall promulgate such rules and regulations as the Director considers necessary and appropriate to carry out the requirements of this title and the amendments made by this title.\n**(3) Comments by the Election Assistance Commission**\nThe Election Assistance Commission shall timely submit comments with respect to any proposed regulations promulgated by the Director under this subsection.\n##### (h) Interim authority pending appointment and confirmation of Director\n**(1) Authority of Director of Office of Management and Budget**\nNotwithstanding subsection (b), during the transition period, the Director of the Office of Management and Budget is authorized to perform the functions of the Office under this Act, and shall act for all purposes as, and with the full powers of, the Director.\n**(2) Interim administrative services**\n**(A) Authority of Office of Management and Budget**\nDuring the transition period, the Director of the Office of Management and Budget may provide administrative services necessary to support the Office.\n**(B) Termination of authority; permitting extension**\nThe Director of the Office of Management and Budget shall cease providing interim administrative services under this paragraph upon the expiration of the transition period, except that the Director of the Office of Management and Budget may continue to provide such services after the expiration of the transition period if the Director and the Director of the Office of Management and Budget jointly transmit to the Committee on House Administration of the House of Representatives and the Committee on Rules and Administration of the Senate\u2014\n**(i)**\na written determination that an orderly implementation of this Act is not feasible by the expiration of the transition period;\n**(ii)**\nan explanation of why an extension is necessary for the orderly implementation of this Act;\n**(iii)**\na description of the period during which the Director of the Office of Management and Budget shall continue providing services under the authority of this subparagraph; and\n**(iv)**\na description of the steps that will be taken to ensure an orderly and timely implementation of this Act during the period described in clause (iii).\n**(3) Transition period defined**\nIn this subsection, the transition period is the period which begins on the date of the enactment of this Act and ends on the date on which the first Director is appointed.\n**(4) Limit on length of period of interim authorities**\nNotwithstanding any other provision of this subsection, the Director of the Office of Management and Budget may not exercise any authority under this subsection after the expiration of the 24-month period which begins on the date of the enactment of this Act.\n##### (i) Authorization of appropriations\nThere are authorized to be appropriated from the Trust Fund such sums as may be necessary to carry out the activities of the Office for fiscal year 2026 and each succeeding fiscal year.\nII\nState Election Assistance and Innovation Trust Fund\n#### 201. State Election Assistance and Innovation Trust Fund\n##### (a) Establishment\nThere is established in the Treasury a fund to be known as the State Election Assistance and Innovation Trust Fund .\n##### (b) Contents\nThere is hereby appropriated to the Trust Fund $2,500,000,000 for each of fiscal years 2026 through 2035.\n##### (c) Use of funds\nAmounts in the Trust Fund shall be used to make payments and allocations under the Program and to carry out the activities of the Office.\n##### (d) Acceptance of gifts\nThe Office may accept gifts or bequests for deposit into the Trust Fund.\nIII\nGeneral Provisions\n#### 301. Definitions\nIn this Act, the following definitions apply:\n**(1)**\nThe term chief State election official has the meaning given such term in section 253(e) of the Help America Vote Act of 2002 ( 52 U.S.C. 21003(e) ).\n**(2)**\nThe term Director means the Director of the Office.\n**(3)**\nThe term Indian lands includes\u2014\n**(A)**\nIndian country, as defined under section 1151 of title 18, United States Code;\n**(B)**\nany land in Alaska owned, pursuant to the Alaska Native Claims Settlement Act ( 43 U.S.C. 1601 et seq. ), by an Indian Tribe that is a Native village (as defined in section 3 of that Act ( 43 U.S.C. 1602 )) or by a Village Corporation that is associated with an Indian Tribe (as defined in section 3 of that Act ( 43 U.S.C. 1602 ));\n**(C)**\nany land on which the seat of the Tribal government is located; and\n**(D)**\nany land that is part or all of a Tribal designated statistical area associated with an Indian Tribe, or is part or all of an Alaska Native village statistical area associated with an Indian Tribe, as defined by the Census Bureau for the purposes of the most recent decennial census.\n**(4)**\nThe term Office means the Office of Democracy Advancement and Innovation established under section 105.\n**(5)**\nThe term Program means the Democracy Advancement and Innovation Program established under section 101.\n**(6)**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands.\n**(7)**\nThe term Trust Fund means the State Election Assistance and Innovation Trust Fund established under section 201.\n#### 302. Rule of construction regarding calculation of deadlines\n##### (a) In general\nWith respect to the calculation of any period of time for the purposes of a deadline in this Act, the last day of the period shall be included in such calculation, unless such day is a Saturday, a Sunday, or a legal public holiday, in which case the period of such deadline shall be extended until the end of the next day which is not a Saturday, a Sunday, or a legal public holiday.\n##### (b) Legal public holiday defined\nFor the purposes of this section, the term legal public holiday means a day described in section 6103(a) of title 5, United States Code.\n#### 303. Severability\nIf any provision of this Act or any amendment made by this Act, or the application of any such provision or amendment to any person or circumstance, is held to be unconstitutional, the remainder of such Act and amendments made by such Act and the application of such provision or amendment to any other person or circumstance, shall not be affected by the holding.",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "4910",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Sustaining Our Democracy Act",
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
        "updateDate": "2025-09-15T18:05:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s2588",
          "measure-number": "2588",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2588v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sustaining Our Democracy Act</strong></p><p>This bill establishes and provides funds through FY2035 for the State Election Assistance and Innovation Trust Fund for purposes of promoting election activities.</p><p>Specifically, the bill establishes the Democracy Advancement and Innovation Program, through which the Office of Democracy Advancement and Innovation (also established by this bill) shall make allocations to states for carrying out democracy promotion activities. These activities include improving the administration of federal elections, recruiting and training nonpartisan election officials and poll workers, and increasing voting access.</p><p>The bill requires each state, in order to receive allocated funds, to (1) submit a plan for approval that describes how the state will distribute resources and carry out democracy promotion activities, and (2) establish uniform and nondiscriminatory state-based administrative complaint procedures.</p><p>The bill prohibits states from using funds for certain activities, including any activity that diminishes the ability of any eligible voter to participate in the electoral process.</p>"
        },
        "title": "Sustaining Our Democracy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2588.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sustaining Our Democracy Act</strong></p><p>This bill establishes and provides funds through FY2035 for the State Election Assistance and Innovation Trust Fund for purposes of promoting election activities.</p><p>Specifically, the bill establishes the Democracy Advancement and Innovation Program, through which the Office of Democracy Advancement and Innovation (also established by this bill) shall make allocations to states for carrying out democracy promotion activities. These activities include improving the administration of federal elections, recruiting and training nonpartisan election officials and poll workers, and increasing voting access.</p><p>The bill requires each state, in order to receive allocated funds, to (1) submit a plan for approval that describes how the state will distribute resources and carry out democracy promotion activities, and (2) establish uniform and nondiscriminatory state-based administrative complaint procedures.</p><p>The bill prohibits states from using funds for certain activities, including any activity that diminishes the ability of any eligible voter to participate in the electoral process.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2588"
    },
    "title": "Sustaining Our Democracy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sustaining Our Democracy Act</strong></p><p>This bill establishes and provides funds through FY2035 for the State Election Assistance and Innovation Trust Fund for purposes of promoting election activities.</p><p>Specifically, the bill establishes the Democracy Advancement and Innovation Program, through which the Office of Democracy Advancement and Innovation (also established by this bill) shall make allocations to states for carrying out democracy promotion activities. These activities include improving the administration of federal elections, recruiting and training nonpartisan election officials and poll workers, and increasing voting access.</p><p>The bill requires each state, in order to receive allocated funds, to (1) submit a plan for approval that describes how the state will distribute resources and carry out democracy promotion activities, and (2) establish uniform and nondiscriminatory state-based administrative complaint procedures.</p><p>The bill prohibits states from using funds for certain activities, including any activity that diminishes the ability of any eligible voter to participate in the electoral process.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2588"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2588is.xml"
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
      "title": "Sustaining Our Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sustaining Our Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a democracy advancement and innovation program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:22Z"
    }
  ]
}
```
