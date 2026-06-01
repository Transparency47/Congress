# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1310?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1310
- Title: No Tax Breaks for Union Busting (NTBUB) Act
- Congress: 119
- Bill type: S
- Bill number: 1310
- Origin chamber: Senate
- Introduced date: 2025-04-04
- Update date: 2026-04-08T16:49:21Z
- Update date including text: 2026-04-08T16:49:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-04: Introduced in Senate
- 2025-04-04 - IntroReferral: Introduced in Senate
- 2025-04-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-04: Introduced in Senate

## Actions

- 2025-04-04 - IntroReferral: Introduced in Senate
- 2025-04-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-04",
    "latestAction": {
      "actionDate": "2025-04-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1310",
    "number": "1310",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Lujan, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "No Tax Breaks for Union Busting (NTBUB) Act",
    "type": "S",
    "updateDate": "2026-04-08T16:49:21Z",
    "updateDateIncludingText": "2026-04-08T16:49:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-04",
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
          "date": "2025-04-04T22:00:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "CT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-04",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
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
      "sponsorshipDate": "2025-04-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1310is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1310\nIN THE SENATE OF THE UNITED STATES\nApril 4, 2025 Mr. Luj\u00e1n (for himself, Ms. Smith , Mr. Booker , Ms. Baldwin , Mr. Blumenthal , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mr. Heinrich , Ms. Hirono , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Slotkin , Mr. Van Hollen , Ms. Warren , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to end the tax subsidy for employer efforts to influence their workers\u2019 exercise of their rights around labor organizations and engaging in collective action.\n#### 1. Short title\nThis Act may be cited as the No Tax Breaks for Union Busting (NTBUB) Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe National Labor Relations Act ( 29 U.S.C. 151 et seq. ) declares that it is the right of employees to form, join, or assist labor organizations.\n**(2)**\nThe National Labor Relations Act further declares that it is the policy of the United States to eliminate the causes of certain substantial obstructions to the free flow of commerce and to mitigate and eliminate these obstructions when they have occurred by encouraging the practice and procedure of collective bargaining and by protecting the exercise by workers of full freedom of association, self-organization, and designation of representatives of their own choosing . . . .\n**(3)**\nDespite Congress\u2019 intention to give workers full agency in these matters, many employers regularly choose to involve themselves, lawfully or unlawfully, in the decisions of their employees about whether to avail themselves of their rights under the National Labor Relations Act and the Railway Labor Act ( 45 U.S.C. 151 et seq. ).\n**(4)**\nEmployers frequently violate labor laws around organizing and collective action. The Economic Policy Institute finds that in approximately 4 of 10 labor organization elections in 2016\u20132017 employers were charged with committing an unfair labor practice. Among larger bargaining units of 61 employees or more, over 54 percent of elections have an unfair labor practice charge.\n**(5)**\nIn practice, these unfair labor practices often include charges such as employees being illegally fired for labor organization activity, refusal to bargain in good faith with labor organizations, or coercion and intimidation. Employers also frequently use captive audience meetings, workplace surveillance, and other lawful or unlawful tactics to sway labor organization elections.\n**(6)**\nWhether or not there are charges of unlawful behavior, employers spend millions of dollars to sway the opinions of their employees with respect to whether or how to exercise their rights under the National Labor Relations Act and the Railway Labor Act. According to the Economic Policy Institute, companies spent $340,000,000 yearly on outside consultants to sway their workers' opinions about labor organization activities. This and other spending interfere with the United States' goal of encouraging the practice and procedure of collective bargaining .\n**(7)**\nThe Internal Revenue Code of 1986 has long recognized that spending by businesses with the purpose of influencing the general public with respect to elections, while it may be lawful, is not tax deductible. Congress should extend that principle to spending done by employers to influence workers\u2019 elections and collective bargaining decisions. These free choices to exercise the rights to engage in collective bargaining, labor organization representation, and other lawful collective activities should be made without taxpayer subsidies of undue outside influence from employers.\n#### 3. Denial of deduction for attempting to influence employees with respect to labor organizations or labor organization activities\n##### (a) In general\nSection 162(e)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by adding at the end the following new subparagraph:\n(E) any attempt to influence the taxpayer's employees with respect to labor organizations or labor organization activities, including with respect to the opinion of such employees regarding such organizations or activities. .\n##### (b) Labor organizations; labor organization activities defined\nSection 162(e) of the Internal Revenue Code of 1986 is amended by redesignating paragraph (6) as paragraph (7) and by inserting after paragraph (5) the following new paragraph:\n(6) Labor organizations and labor organization activity defined For purposes of this subsection\u2014 (A) Labor organization The term labor organization has the meaning given such term in section 3 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 402 ). (B) Labor organization activity (i) In general The term labor organization activity means labor organization elections, labor disputes, collective actions, and such other related activities identified by the Secretary. (ii) Other terms For purposes of clause (i)\u2014 (I) Collective action The term collective action means any action, including collective bargaining, described in section 7 of the National Labor Relations Act ( 29 U.S.C. 157 ) or any action that is a right of employees or labor organizations under the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (II) Labor dispute The term labor dispute has the meaning given such term under section 3 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 402 ). (III) Labor organization election The term labor organization election means any election described in section 9 of the National Labor Relations Act ( 29 U.S.C. 159 ) or section 2 of the Railway Labor Act ( 45 U.S.C. 152 ). .\n##### (c) Special rules\n**(1) In general**\nSection 162(e)(4) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Expenses relating to labor organizations or labor organization activities (i) In general For purposes of paragraph (1)(E), amounts paid or incurred in connection with attempting to influence the taxpayer's employees with respect to labor organizations or labor organization activities include\u2014 (I) any amount paid or incurred directly or indirectly by the taxpayer, including wages and other general and administrative costs, in connection with an action that results in\u2014 (aa) a complaint issued under section 10 of the National Labor Relations Act ( 29 U.S.C. 160 ) against the taxpayer for an unfair labor practice under section 8(a) of such Act ( 29 U.S.C. 158(a) ), (bb) a settlement offer related to an investigation by the National Labor Relations Board of a charge of an unfair labor practice under section 8(a) of such Act ( 29 U.S.C. 158(a) ) that results in a settlement of such charge without issuance of a complaint under section 10 of such Act ( 29 U.S.C. 160 ), or (cc) a finding of interference, influence, or coercion by a Federal court under section 2 of the Railway Labor Act ( 45 U.S.C. 152 ), (II) any amount paid or incurred directly or indirectly by the taxpayer, including wages and other general and administrative costs, in producing, conducting, or attending any meeting or training\u2014 (aa) which includes employees of the taxpayer who are or who could become members of a unit appropriate for the purposes of collective bargaining, and (bb) at which labor organizations or a labor organization activity is discussed, and (III) any amount which is required to be reported under the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ). (ii) Exceptions The following amounts shall not be treated as amounts paid or incurred in connection with attempting to influence the taxpayer's employees with respect to labor organizations or labor organization activities under paragraph (1)(E): (I) Amounts paid or incurred for communications or negotiations directly with the designated or selected representative of the employees of the taxpayer described in section 9(a) of the National Labor Relations Act ( 29 U.S.C. 159(a) ) or under the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (II) Amounts paid or incurred for communications directly with shareholders, as may be required under section 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ). (III) Amounts paid or incurred for communications or consultations by the taxpayer in the process of voluntarily recognizing a labor organization as a representative in accordance with section 9 of the National Labor Relations Act ( 29 U.S.C. 159 ). (IV) Amounts paid or incurred with respect to the operation of a labor-management partnership described in a collective bargaining agreement in effect between a representative of employees of the taxpayer and the taxpayer, including a labor management committee established pursuant to section 205A(a) of the Labor Management Relations Act, 1947 ( 29 U.S.C. 175a(a) ). (V) Amounts paid or incurred for communications or consultations related to the operation of a grievance procedure described in a collective bargaining agreement in effect between a representative of employees of the taxpayer and the taxpayer. (VI) Amounts paid or incurred by a labor organization. (VII) Amounts paid or incurred for communication materials, including visual or audio media, required to be posted for, or provided to, employees of the taxpayer by law, including under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ) or the Railway Labor Act ( 45 U.S.C. 151 et seq. ). (VIII) Amounts paid or incurred relating to a complaint which is issued by the National Labor Relations Board and which is set aside in full in accordance with subsection (e) or (f) of section 10 of such Act. .\n**(2) Regulatory authority**\n**(A) In general**\nSection 162(e) of such Code, as amended by subsection (b), is amended by redesignating paragraph (7) as paragraph (8) and by inserting after paragraph (6) the following new paragraph:\n(7) Regulations The Secretary shall prescribe such guidance, rules, or regulations as are necessary to carry out the purposes of this subsection, including rules relating to the timing of any deductions in connection with amounts described in paragraph (4)(D)(ii)(VIII). .\n**(B) Timing**\nNot later than the date that is 240 days after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall prescribe guidance, rules, or regulations with respect to the application of the amendments made by this Act.\n##### (d) Information reporting\n**(1) Certain information included in tax returns**\n**(A) In general**\nPart I of subchapter B of chapter 68 is amended by adding at the end the following new section:\n6720D. Failure to include certain information with respect to employer activities relating to labor organizations (a) In general If any taxpayer who makes expenditures described in section 162(e)(1)(E) fails to provide with the return of tax for the taxable year to which such expenditures relate the information provided in subsection (c) with respect to such expenditures, or who fails to provide all of the information required under subsection (b) or fails to provide correct information, shall pay a penalty in the amount determined under subsection (b). (b) Determination of penalty amount (1) In general The amount of the penalty under this section for any failure described in subsection (a) shall be the greater of\u2014 (A) $10,000, or (B) the product of $1,000 and the number of full time equivalent employees of the employer (as determined under section 45R(d)(2)). (2) Increased penalty where failure continues (A) In general If any failure described in subsection (a)(1) continues for more than 90 days after the day on which the Secretary mails notice of such failure to the taxpayer, the taxpayer shall pay a penalty (in addition to the amount of any penalty under paragraph (1)) equal to the amount determined under paragraph (1) for each 30-day period (or fraction thereof) during which such failure continues after the expiration of such 90-day period. (B) Limitation The penalty imposed under this paragraph with respect to any failure shall not exceed $100,000. (c) Information To be provided The information required under this subsection shall include\u2014 (1) the dates that such activities described in section 162(e)(1)(E) took place, (2) a statement indicating whether the activity was an activity described in item (aa), (bb), or (cc) of section 162(e)(4)(D)(i)(I), (3) the amounts paid or incurred for such activities, (4) a copy of any disclosures which are required to be reported under the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 401 et seq. ), and (5) such other information as the Secretary may prescribe. (d) Reasonable cause exception No penalty shall be imposed by this section on any failure which is shown to be due to reasonable cause and not due to willful neglect. .\n**(B) Clerical amendment**\nThe table of sections for part I of subchapter B of chapter 68 is amended by adding at the end the following new item:\nSec. 6720D. Failure to include certain information with respect to employer activities relating to labor organizations. .\n**(2) Third-party information reporting**\n**(A) In general**\nSubpart A of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by inserting after section 6039J the following new section:\n6039K. Information with respect to certain employer activities relating to labor organizations (a) In general Any person conducting activities described in section 162(e)(1)(E) on behalf of another person shall file a return (at such time and in such manner as the Secretary may by regulations prescribe, which includes the information described in subsection (b)). (b) Information To be provided Information required under subsection (a) shall include\u2014 (1) the person on behalf of whom the activities described in section 162(e)(1)(E) were performed, (2) the dates that such activities described in such section took place, (3) a statement indicating whether the activity was an activity described in item (aa), (bb), or (cc) of section 162(e)(4)(D)(i)(I), (4) the amounts paid or incurred for such activities, and (5) such other information as the Secretary may prescribe. .\n**(B) Penalty**\nSubparagraph (B) of section 6724(d)(1) of such Code is amended\u2014\n**(i)**\nby striking or at the end of clause (xxvii),\n**(ii)**\nby striking and at the end of clause (xxxviii) and inserting or , and\n**(iii)**\nby adding at the end the following new clause:\n(xxvix) section 6039K (relating to information with respect to certain employer activities relating to labor organizations), and .\n**(C) Clerical amendment**\nThe table of sections for subpart A of part III of subchapter A of chapter 61 of such Code is amended by inserting after the item relating to section 6039J the following new item:\nSec. 6039K. Information with respect to certain employer activities relating to labor organizations. .\n##### (e) Conforming amendments\n**(1)**\nThe heading for subsection (e) of section 162 of the Internal Revenue Code of 1986 is amended by striking and political expenditures and inserting , political expenditures, and labor organization expenditures .\n**(2)**\nThe heading of subparagraph (C) of section 162(e)(4) of such Code is amended by striking and political activities and inserting , political, and labor organization activities .\n##### (f) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after the date that is 240 days after the date of the enactment of this Act.",
      "versionDate": "2025-04-04",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2692",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T16:44:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-04",
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
          "measure-id": "id119s1310",
          "measure-number": "1310",
          "measure-type": "s",
          "orig-publish-date": "2025-04-04",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1310v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-04-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>"
        },
        "title": "No Tax Breaks for Union Busting (NTBUB) Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1310.xml",
    "summary": {
      "actionDate": "2025-04-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s1310"
    },
    "title": "No Tax Breaks for Union Busting (NTBUB) Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Tax Breaks for Union Busting (NTBUB) Act</strong></p><p>This bill excludes from the tax deduction for ordinary and necessary business expenses amounts paid or incurred to influence employees with respect to labor organizations or labor organization activities. The bill also imposes information reporting requirements related to such expenses and imposes penalties for failure to comply.\u00a0</p><p>Under the bill, amounts paid to influence employees with respect to labor organizations include amounts paid (including wages and other costs) </p><ul><li>in connection with an action that results in a complaint or settlement related to an unfair labor practice or a finding of interference, influence, or coercion related to railway employees\u2019 rights to organize and bargain collectively;</li><li>for\u00a0any meeting or training attended by employees and at which labor organizations are discussed; and</li><li>that require\u00a0certain employer disclosures and financial reporting.</li></ul><p>(Some exceptions apply.)\u00a0</p><p>The bill requires employers to file a return reporting certain information related to expenses paid to influence employees with respect to labor organizations and imposes a penalty for noncompliance. The amount of the penalty is the greater of (1) $10,000, or (2) $1,000 multiplied by the number full-time equivalent employees. Additional penalties apply for\u00a0violations that continue for more than 90 days.\u00a0</p><p>The bill also imposes information reporting requirements on persons conducting activities on behalf of another person to influence employees with respect to labor organizations.</p><p>The bill allows certain penalties for noncompliance with the reporting requirements to be waived if noncompliance is due to reasonable cause and not willful neglect.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s1310"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1310is.xml"
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
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax Breaks for Union Busting (NTBUB) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to end the tax subsidy for employer efforts to influence their workers' exercise of their rights around labor organizations and engaging in collective actions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:32Z"
    }
  ]
}
```
