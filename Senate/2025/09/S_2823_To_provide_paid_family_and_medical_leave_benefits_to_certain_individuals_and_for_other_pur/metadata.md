# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2823
- Title: FAMILY Act
- Congress: 119
- Bill type: S
- Bill number: 2823
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-12-05T21:38:06Z
- Update date including text: 2025-12-05T21:38:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2823",
    "number": "2823",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "FAMILY Act",
    "type": "S",
    "updateDate": "2025-12-05T21:38:06Z",
    "updateDateIncludingText": "2025-12-05T21:38:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T21:56:47Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "DE"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "HI"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-09-16",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2823is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2823\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Mrs. Gillibrand (for herself, Mr. Wyden , Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Mr. Coons , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Ms. Hassan , Mr. Heinrich , Ms. Hirono , Mr. Kelly , Mr. Kim , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mr. Murphy , Mrs. Murray , Mr. Padilla , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mr. Schumer , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Warnock , Ms. Warren , Mr. Welch , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide paid family and medical leave benefits to certain individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family and Medical Insurance Leave Act or the FAMILY Act .\n#### 2. Definitions\nIn this Act:\n**(1) Caregiving hour**\n**(A) In general**\nThe term caregiving hour means, with respect to an individual, a 1-hour period during which the individual engaged in qualified caregiving.\n**(B) Limitations**\nWith respect to any benefit period, an individual may not exceed a number of caregiving hours equal to 12 times the number of hours in a regular workweek of the individual (as determined under subparagraph (C)).\n**(C) Number of hours in a regular workweek**\nFor purposes of this Act, the number of hours in a regular workweek of an individual shall be the number of hours that the individual regularly works in a week for all employers or as a self-employed individual (or regularly worked in the case of an individual who is no longer working or whose total weekly hours of work have been reduced) during the month before the individual\u2019s benefit period begins (or prior to such month, if applicable in the case of an individual who is no longer working or whose total weekly hours of work have been reduced).\n**(2) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(3) Deputy Commissioner**\nThe term Deputy Commissioner means the Deputy Commissioner who heads the Office of Paid Family and Medical Leave established under section 3(a).\n**(4) Eligible individual**\nThe term eligible individual means an individual who is entitled to a benefit under section 4 for a particular month, upon filing an application for such benefit for such month.\n**(5) National average wage index**\nThe term national average wage index has the meaning given such term in section 209(k)(1) of the Social Security Act ( 42 U.S.C. 409(k)(1) ).\n**(6) Qualified caregiving**\n**(A) In general**\nThe term qualified caregiving means any activity engaged in by an individual, other than regular employment, for a qualifying reason.\n**(B) Qualifying reason**\n**(i) In general**\nFor purposes of subparagraph (A), the term qualifying reason means any of the following reasons for taking leave:\n**(I)**\nAny reason for which an eligible employee would be entitled to leave under subparagraph (A), (B), or (E) of paragraph (1) of section 102(a) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a) ).\n**(II)**\nIn order to care for a qualified family member of the individual, if such qualified family member has a serious health condition.\n**(III)**\nBecause of a serious health condition that makes the individual unable to perform the services required under the terms of their regular employment.\n**(IV)**\nBecause the individual, or a qualified family member, is a victim of family violence or a qualifying act of violence, if the leave is for the individual to do any of the following or to assist the individual\u2019s qualified family member to, as a result of such violence, do any of the following:\n**(aa)**\nSeek, receive, or secure counseling.\n**(bb)**\nSeek or secure temporary or permanent relocation or take steps to secure an existing home.\n**(cc)**\nSeek, receive, or follow up on assistance from a victim services organization or agency providing services to victims.\n**(dd)**\nSeek legal assistance or attend legal proceedings, including preparation for or participation in any related administrative, civil, or criminal legal proceedings or other related activities.\n**(ee)**\nSeek medical attention for physical or psychological injury or disability caused or aggravated by the qualifying act of violence.\n**(ff)**\nEnroll in a new school or care arrangement.\n**(gg)**\nTake other steps necessary to protect or restore their physical, mental, emotional, spiritual, and economic well-being or the well-being of a qualified family member recovering from a qualifying act of violence.\n**(ii) Qualified family member; serious health condition**\nIn this subparagraph:\n**(I) Qualified family member**\nThe term qualified family member means, with respect to an individual\u2014\n**(aa)**\na spouse (including a domestic partner in a civil union or other registered domestic partnership recognized by a State) or a parent of such spouse;\n**(bb)**\na child (regardless of age) or a child\u2019s spouse;\n**(cc)**\na parent or a parent\u2019s spouse;\n**(dd)**\na sibling or a sibling\u2019s spouse;\n**(ee)**\na grandparent, a grandchild, or a spouse of a grandparent or grandchild; and\n**(ff)**\nany other individual who is related by blood or affinity and whose association with the employee is equivalent of a family relationship.\n**(II) Serious health condition**\nThe term serious health condition has the meaning given such term in section 101(11) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(11) ).\n**(iii) Treatment of individuals covered by legacy State comprehensive paid leave program**\n**(I) In general**\nFor purposes of subparagraph (A), an activity engaged in by an individual shall not be considered as other than regular employment if, for the time during which the individual was so engaged, the individual is taking leave from covered employment under the law of a legacy State (as defined in section 4(c)).\n**(II) Unemployed**\nIn the case of an individual who is no longer employed, such individual shall be treated, for purposes of clause (i), as taking leave from covered employment under the law of a legacy State (as so defined) with respect to the portion of the time during which the individual was engaged in an activity for a qualifying reason corresponding to the share of the individual\u2019s workweek that was in covered employment under the law of a legacy State (as so defined).\n**(C) Other definitions**\nFor purposes of this paragraph:\n**(i) Child**\nThe term child means, regardless of age, a biological, foster, or adopted child, a stepchild, a child of a domestic partner, a legal ward, or a child of a person standing in loco parentis.\n**(ii) Domestic partner**\n**(I) In general**\nThe term domestic partner , with respect to an individual, means another individual with whom the individual is in a committed relationship.\n**(II) Committed relationship defined**\nThe term committed relationship means a relationship between 2 individuals, each at least 18 years of age, in which each individual is the other individual\u2019s sole domestic partner and both individuals share responsibility for a significant measure of each other\u2019s common welfare. The term includes any such relationship between 2 individuals, including individuals of the same sex, that is granted legal recognition by a State or political subdivision of a State as a marriage or analogous relationship, including a civil union or domestic partnership.\n**(iii) Dating violence**\nThe term dating violence has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(iv) Domestic violence**\nThe term domestic violence has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ), except that the reference in such section to the term jurisdiction receiving grant funding shall be deemed to mean the jurisdiction in which the victim lives or the jurisdiction in which the employer involved is located.\n**(v) Parent**\nThe term parent means a biological, foster, or adoptive parent of an employee, a stepparent of an employee, parent-in-law, parent of a domestic partner, or a legal guardian or other person who stood in loco parentis to an employee when the employee was a child.\n**(vi) Qualifying act of violence**\nThe term qualifying act of violence means an act, conduct, or pattern of conduct that could constitute any of the following:\n**(I)**\nDating violence.\n**(II)**\nDomestic violence.\n**(III)**\nFamily violence.\n**(IV)**\nSexual assault.\n**(V)**\nSex trafficking.\n**(VI)**\nStalking.\n**(VII)**\nOther forms of gender-based violence or harassment.\n**(VIII)**\nAn act, conduct, or pattern of conduct\u2014\n**(aa)**\nin which an individual causes or threatens to cause bodily injury or death to another individual;\n**(bb)**\nin which an individual exhibits, draws, brandishes, or uses a firearm, or other dangerous weapon, with respect to another individual; or\n**(cc)**\nin which an individual uses, or makes a reasonably perceived or actual threat to use, force against another individual to cause bodily injury or death.\n**(vii) Sexual assault**\nThe term sexual assault has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(viii) Sex trafficking**\nThe term sex trafficking has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(ix) Spouse**\nThe term spouse , with respect to an employee, has the meaning given such term by the marriage laws of the State in which the marriage was celebrated.\n**(x) Stalking**\nThe term stalking has the meaning given the term in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n**(xi) Victim services organization**\nThe term victim services organization means a nonprofit, nongovernmental organization that provides assistance to victims of qualifying acts of violence or advocates for such victims, including\u2014\n**(I)**\na rape crisis center;\n**(II)**\nan organization carrying out a prevention or treatment program for qualifying acts of violence;\n**(III)**\nan organization operating a shelter or providing counseling services; and\n**(IV)**\na legal services organization or other organization providing assistance through the legal process.\n**(7) Self-employment income**\nThe term self-employment income has the same meaning as such term in section 211(b) of such Act ( 42 U.S.C. 411(b) ).\n**(8) State**\nThe term State means any State of the United States or the District of Columbia or any territory or possession of the United States.\n**(9) Wages**\nThe term wages has the meaning given such term in section 3121(a) of the Internal Revenue Code of 1986 for purposes of the taxes imposed by sections 3101(b) and 3111(b) of such Code (without regard to section 3121(u)(2)(C) of such Code), except that such term also includes\u2014\n**(A)**\ncompensation, as defined in section 3231(e) of such Code for purposes of the Railroad Retirement Tax Act; and\n**(B)**\nunemployment compensation, as defined in section 85(b) of such Code.\n#### 3. Office of Paid Family and Medical Leave\n##### (a) Establishment of Office\nThere is established within the Social Security Administration an office to be known as the Office of Paid Family and Medical Leave. The Office shall be headed by a Deputy Commissioner who shall be appointed by the Commissioner.\n##### (b) Responsibilities of Deputy Commissioner\nThe Commissioner, acting through the Deputy Commissioner, shall be responsible for\u2014\n**(1)**\nhiring personnel and making employment decisions with regard to such personnel;\n**(2)**\nissuing such regulations as may be necessary to carry out the purposes of this Act;\n**(3)**\nentering into cooperative agreements with other agencies and departments to ensure the efficiency of the administration of the program;\n**(4)**\ndetermining eligibility for family and medical leave insurance benefits under section 4;\n**(5)**\ndetermining benefit amounts for each month of such eligibility and making timely payments of such benefits to entitled individuals in accordance with such section;\n**(6)**\nestablishing and maintaining a system of records relating to the administration of such section;\n**(7)**\npreventing fraud and abuse relating to such benefits;\n**(8)**\nproviding information on request regarding eligibility requirements, the claims process, benefit amounts, maximum benefits payable, notice requirements, nondiscrimination rights, confidentiality, coordination of leave under this Act and other laws, collective bargaining agreements, and employer policies;\n**(9)**\nannually providing employers a notice to inform employees of the availability of such benefits;\n**(10)**\nannually making available to the public a report that includes the number of individuals who received such benefits, the purposes for which such benefits were received, and an analysis of utilization rates of such benefits by gender, race, ethnicity, and income levels; and\n**(11)**\ntailoring culturally and linguistically competent education and outreach toward increasing utilization rates of benefits under such section.\n##### (c) Availability of data\nNotwithstanding any other provision of law, the Commissioner shall make available to the Deputy Commissioner such data as the Commissioner determines necessary to enable the Deputy Commissioner to effectively carry out the responsibilities described in subsection (b).\n##### (d) Datasharing\nThe Commissioner and the heads of Federal agencies shall make good faith efforts to enter into datasharing agreements to enable the Deputy Commissioner to effectively carry out the responsibilities described in subsection (b).\n##### (e) Report to Congress\nNot later than 12 months after the date of enactment of this Act, the Commissioner shall submit to Congress a report including information on the following:\n**(1)**\nDatabases maintained by Federal agencies that contain information necessary to carry out the purposes of this Act, including information on any congressional action needed to permit the Commissioner to access such databases for such purposes.\n**(2)**\nThe feasibility of expediting the review of applications under paragraph (1) of section 4(f) and the payment of monthly benefit payments under paragraph (2) of such section, including the effects of establishing shorter time frames for such reviews and payment in statute.\n#### 4. Family and Medical Leave Insurance benefit payments\n##### (a) In general\n**(1) Requirements**\nEvery individual who\u2014\n**(A)**\nhas filed an application for a family and medical leave insurance benefit in accordance with subsection (d);\n**(B)**\nwas engaged in qualified caregiving, or anticipates being so engaged, during the period that begins 90 days before the date on which such application is filed and ends 30 days after such date;\n**(C)**\nhas wages or self-employment income at any time during the period\u2014\n**(i)**\nbeginning with the most recent calendar quarter that ends at least 4 months prior to the beginning of the individual\u2019s benefit period specified in subsection (c); and\n**(ii)**\nending with the month before the month in which such benefit period begins; and\n**(D)**\nhas at least the specified amount of wages and self-employment income during the most recent 8-calendar quarter period that ends at least 4 months prior to the beginning of the individual\u2019s benefit period specified in subsection (c),\nshall be entitled to such a benefit for each month in such benefit period.\n**(2) Specified amount**\nFor purposes of paragraph (1)(D), the specified amount shall be\u2014\n**(A)**\nif the benefit period begins in calendar year 2026, $2,000; and\n**(B)**\nif the benefit period begins in any calendar year after 2026, an amount equal to the greater of\u2014\n**(i)**\nthe specified amount applicable for the preceding calendar year; or\n**(ii)**\nan amount equal to the product of\u2014\n**(I)**\n$2,000; multiplied by\n**(II)**\nan amount equal to the quotient of\u2014\n**(aa)**\nthe national average wage index for the second calendar year preceding such calendar year; divided by\n**(bb)**\nthe national average wage index for 2024.\n##### (b) Benefit amount\n**(1) In general**\nExcept as otherwise provided in this subsection, the benefit amount to which an individual is entitled under this section for a month shall be an amount equal to the product of\u2014\n**(A)**\nthe greater of\u2014\n**(i)**\nthe lesser of\u2014\n**(I)**\nan amount equal to the monthly benefit rate determined under paragraph (2); and\n**(II)**\nthe maximum benefit amount determined under paragraph (3); and\n**(ii)**\nthe minimum benefit amount determined under paragraph (3); and\n**(B)**\nthe quotient (not greater than 1) obtained by dividing the number of caregiving hours of the individual in such month by the product of\u2014\n**(i)**\nthe number of hours in a regular workweek of the individuals; and\n**(ii)**\nthe number of workweeks (including partial workweeks) in such month.\n**(2) Monthly benefit rate**\n**(A) In general**\nFor purposes of this subsection, the monthly benefit rate of an individual shall be an amount equal to the sum of\u2014\n**(i)**\n85 percent of the individual\u2019s average monthly earnings to the extent that such earnings do not exceed the amount established for purposes of this clause by subparagraph (B);\n**(ii)**\n69 percent of the individual\u2019s average monthly earnings to the extent that such earnings exceed the amount established for purposes of clause (i) but do not exceed the amount established for purposes of this clause by subparagraph (B); and\n**(iii)**\n50 percent of the individual\u2019s average monthly earnings to the extent that such earnings exceed the amount established for purposes of clause (ii) but do not exceed the amount established for purposes of this clause by subparagraph (B).\n**(B) Amounts established**\n**(i) Initial amounts**\nFor individuals whose benefit period begins in calendar year 2026, the amount established for purposes of clauses (i), (ii), and (iii) of subparagraph (A) shall be $1,257, $3,500, and $6,200, respectively.\n**(ii) Wage indexing**\nFor individuals whose benefit period begins in any calendar year after 2026, each of the amounts so established shall equal the corresponding amount established for the calendar year preceding such calendar year, or, if larger, the product of the corresponding amount established with respect to the calendar year 2026 and the quotient obtained by dividing\u2014\n**(I)**\nthe national average wage index for the second calendar year preceding such calendar year, by\n**(II)**\nthe national average wage index for calendar year 2024.\n**(iii) Rounding**\nEach amount established under clause (ii) for any calendar year shall be rounded to the nearest $1, except that any amount so established which is a multiple of $0.50 but not of $1 shall be rounded to the next higher $1.\n**(C) Average monthly earnings**\nFor purposes of this subsection, the average monthly earnings of an individual shall be an amount equal to 1/12 of the wages and self-employment income of the individual for the calendar year in which such wages and self-employment income are the highest among the most recent 3 calendar years.\n**(3) Maximum and minimum benefit amounts**\n**(A) In general**\nFor individuals who initially become eligible for family and medical leave insurance benefits in the first full calendar year after the date of enactment of this Act, the maximum monthly benefit amount and the minimum monthly benefit amount shall be $4,000 and $580, respectively.\n**(B) Wage indexing**\nFor individuals who initially become eligible for family and medical leave insurance benefits in any calendar year after such first full calendar year the maximum benefit amount and the minimum benefit amount shall be, respectively, the product of the corresponding amount determined with respect to the first calendar year under subparagraph (A) and the quotient obtained by dividing\u2014\n**(i)**\nthe national average wage index for the second calendar year preceding the calendar year for which the determination is made, by\n**(ii)**\nthe national average wage index for the second calendar year preceding the first full calendar year after the date of enactment of this Act.\n**(4) Minimum caregiving hours**\nIn a case in which the number of caregiving hours of an individual for a month is less than 4, the individual shall be deemed to have zero caregiving hours for such month.\n**(5) Reduction in benefit amount on account of receipt of certain benefits**\nA benefit under this section for a month shall be reduced by the amount, if any, in certain benefits (as determined under regulations issued by the Commissioner) as may be otherwise received by an individual. For purposes of the preceding sentence, certain benefits include\u2014\n**(A)**\nperiodic benefits on account of such individual\u2019s total or partial disability under a workmen\u2019s compensation law or plan of the United States or a State; and\n**(B)**\nperiodic benefits on account of an individual\u2019s employment status under an unemployment law or plan of the United States or a State.\n##### (c) Benefit period\n**(1) In general**\nExcept as provided in paragraph (2), the benefit period specified in this subsection is the 12-month period that begins on the 1st day of the 1st month in which the individual\u2014\n**(A)**\nmeets the criteria specified in subparagraphs (A) and (B) of subsection (a)(1); and\n**(B)**\nwould meet the criteria specified in subparagraphs (C) and (D) of such subsection if such subparagraphs were applied by substituting such 12-month period for each reference to the individual's benefit period.\n**(2) Retroactive benefits**\nIn the case of an application for benefits under this section for qualified caregiving in which the individual was engaged at any time during the 90-day period preceding the date on which such application is submitted, the benefit period specified in this subsection shall begin on the later of\u2014\n**(A)**\nthe 1st day of the 1st month in which the individual engaged in such qualified caregiving; or\n**(B)**\nthe 1st day of the 1st month that begins during such 90-day period,\nand shall end on the date that is 365 days after the 1st day of the benefit period.\n##### (d) Application\nAn application for a family and medical leave insurance benefit shall include\u2014\n**(1)**\na statement that the individual was engaged in qualified caregiving, or anticipates being so engaged, during the period that begins 90 days before the date on which the application is submitted or within 30 days after such date;\n**(2)**\nif the qualified caregiving described in the statement in paragraph (1) is engaged in by the individual because of a serious health condition (as defined in subclause (II) of section 2(5)(B)(ii)) of the individual or a qualified family member (as defined in subclause (I) of such section) of the individual, a certification, issued by the health care provider treating such serious health condition, that affirms the information specified in paragraph (1) and contains such information as the Commissioner shall specify in regulations, which shall be no more than the information that is required to be stated under section 103(b) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2613(b) );\n**(3)**\nif such qualified caregiving is engaged in by the individual for any other qualifying reason (as defined in section 2(5)(B)(i)), a certification, issued by a relevant authority determined under regulations issued by the Commissioner, that affirms the circumstances giving rise to such reason; and\n**(4)**\nan attestation from the applicant that his or her employer has been provided with written notice of the individual\u2019s intention to take family or medical leave, if the individual has an employer, or to the Commissioner in all other cases.\n##### (e) Ineligibility; disqualification\n**(1) Ineligibility for benefit**\nAn individual shall be ineligible for a benefit under this section for any month for which the individual is entitled to\u2014\n**(A)**\ndisability insurance benefits under section 223 of the Social Security Act ( 42 U.S.C. 423 ) or a similar permanent disability program under any law or plan of a State or political subdivision or instrumentality of a State (as such terms are used in section 218 of the Social Security Act ( 42 U.S.C. 418 ));\n**(B)**\nmonthly insurance benefits under section 202 of such Act ( 42 U.S.C. 402 ) based on such individual's disability (as defined in section 223(d) of such Act ( 42 U.S.C. 423(d) )); or\n**(C)**\nbenefits under title XVI of such Act ( 42 U.S.C. 1381 et seq. ) based on such individual\u2019s status as a disabled individual (as determined under section 1614 of such Act ( 42 U.S.C. 1382c )).\n**(2) Disqualification**\nAn individual who has been convicted of a violation under section 208 of the Social Security Act ( 42 U.S.C. 408 ) or who has been found to have used false statements to secure benefits under this section, shall be ineligible for benefits under this section for a 1-year period following the date of such conviction.\n##### (f) Review of eligibility and benefit payment determinations\n**(1) Eligibility determinations**\n**(A) In general**\nThe Commissioner shall provide notice to an individual applying for benefits under this section of the initial determination of eligibility for such benefits, and the estimated benefit amount for a month in which four caregiving hours of the individual occur, as soon as practicable after the application is received.\n**(B) Review**\nAn individual may request review of an initial adverse determination with respect to such application at any time before the end of the 20-day period that begins on the date notice of such determination is received, except that such 20-day period may be extended for good cause. As soon as practicable after the individual requests review of the determination, the Commissioner shall provide notice to the individual of a final determination of eligibility for benefits under this section.\n**(2) Benefit payment determinations**\n**(A) In general**\nThe Commissioner shall make any monthly benefit payment to an individual claiming benefits for a month under this section, or provide notice of the reason such payment will not be made if the Commissioner determines that the individual is not entitled to payment for such month, not later than 20 days after the individual\u2019s monthly benefit claim report for such month is received. Such monthly report shall be filed with the Commissioner not later than 15 days after the end of each month.\n**(B) Review**\nIf the Commissioner determines that payment will not be made to an individual for a month, or if the Commissioner determines that payment shall be made based on a number of caregiving hours in the month inconsistent with the number of caregiving hours in the monthly benefit claim report of the individual for such month, the individual may request review of such determination at any time before the end of the 20-day period that begins on the date notice of such determination is received, except that such 20-day period may be extended for good cause. Not later than 20 days after the individual requests review of the determination, the Commissioner shall provide notice to the individual of a final determination of payment for such month, and shall make payment to the individual of any additional amount not included in the initial payment to the individual for such month to which the Commissioner determines the individual is entitled.\n**(3) Burden of proof**\nAn application for benefits under this section and a monthly benefit claim report of an individual shall each be presumed to be true and accurate, unless the Commissioner demonstrates by a preponderance of the evidence that information contained in the application is false.\n**(4) Definition of monthly benefit claim report**\nFor purposes of this subsection, the term monthly benefit claim report means, with respect to an individual for a month, the individual\u2019s report to the Commissioner of the number of caregiving hours of the individual in such month, which shall be filed not later than 15 days after the end of each month.\n**(5) Review**\nAll final determinations of the Commissioner under this subsection shall be reviewable according to the procedures set out in section 205 of the Social Security Act ( 42 U.S.C. 405 ).\n##### (g) Relationship with State law; employer benefits\n**(1) In general**\nThis section does not preempt or supersede any provision of State or local law that authorizes a State or local municipality to provide paid family and medical leave benefits similar to the benefits provided under this section.\n**(2) Greater benefits allowed**\nNothing in this Act shall be construed to diminish the obligation of an employer to comply with any contract, collective bargaining agreement, or any employment benefit program or plan that provides greater paid leave or other leave rights to employees than the rights established under this Act.\n##### (h) Employment and benefits protection and enforcement\n**(1) Employment and benefits protection**\n**(A) In general**\n**(i) Prohibited acts**\nIt shall be unlawful for any person to interfere with, restrain, deny, or retaliate against an individual because of the exercise of, or the attempt to exercise, any right provided under this section, including through\u2014\n**(I)**\ndischarging or in any other manner discriminating against (including retaliating against) an individual because the individual has applied for, indicated an intent to apply for, or received family and medical leave insurance benefits; or\n**(II)**\nusing the application for or the receipt of such benefits as a negative factor in an employment action.\n**(ii) Restoration to position**\nIt shall be interference with the right of an individual for purposes of clause (i) for an employer of the individual to, upon the conclusion of any leave for which the individual received a family and medical leave insurance benefit under this section, fail to\u2014\n**(I)**\nrestore the individual to the position of employment held by the individual when the leave commenced; or\n**(II)**\nrestore the individual to an equivalent position with equivalent employment benefits, pay, and other terms and conditions of employment.\n**(iii) Maintenance of health benefits**\nIt shall be interference with the right of an individual for purposes of clause (i) for an employer of the individual to fail to maintain, for the duration of any leave for which the individual received a family and medical leave insurance benefit under this section, coverage of the individual under any group health plan (as defined in section 5000(b)(1) of the Internal Revenue Code of 1986) at the level and under the conditions coverage would have been provided if the individual had continued in employment continuously for the duration of such leave.\n**(B) Opposing unlawful practices**\nIt shall be unlawful for any employer to discharge or in any other manner discriminate against any individual for opposing any practice made unlawful by this subsection.\n**(C) Interference with proceedings or inquiries**\nIt shall be unlawful for any person to discharge or in any other manner discriminate against any individual because such individual\u2014\n**(i)**\nhas filed any charge, or has instituted or caused to be instituted any proceeding, under or related to this subsection;\n**(ii)**\nhas given, or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this section; or\n**(iii)**\nhas testified, or is about to testify, in any inquiry or proceeding relating to any right provided under this section.\n**(D) Rebuttable presumption of retaliation**\nAny adverse action (including any action described in subparagraph (C) or (D)) taken against an employee within 12 months of the employee taking any leave for which the individual received a family and medical leave insurance benefit under this section shall establish a rebuttable presumption that the action of the employer is retaliating against such employee in violation of subparagraph (A)(i).\n**(E) Non-application for new hires**\nClauses (ii) and (iii) of subparagraph (A) shall not apply to any individual during the 90-day period beginning with the day the individual begins work for an employer.\n**(2) Civil action by an individual**\n**(A) Liability**\nAny person who violates paragraph (1) shall be liable to any individual employed by such person who is affected by the violation\u2014\n**(i)**\nfor damages equal to the sum of\u2014\n**(I)**\nthe amount of\u2014\n**(aa)**\nany wages, salary, employment benefits, or other compensation denied or lost to such individual by reason of the violation; or\n**(bb)**\nin a case in which wages, salary, employment benefits, or other compensation have not been denied or lost to the individual, any actual monetary losses sustained by the individual as a direct result of the violation, such as the cost of providing care, up to a sum equal to 60 calendar days of wages or salary for the individual;\n**(II)**\nthe interest on the amount described in subclause (I) calculated at the prevailing rate; and\n**(III)**\nan additional amount as liquidated damages equal to the sum of the amount described in subclause (I) and the interest described in subclause (II), except that if a person who has violated paragraph (1) proves to the satisfaction of the court that the act or omission which violated paragraph (1) was in good faith and that the person had reasonable grounds for believing that the act or omission was not a violation of paragraph (1), such court may, in the discretion of the court, reduce the amount of the liability to the amount and interest determined under subclauses (I) and (II), respectively; and\n**(ii)**\nfor such equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(B) Right of action**\nAn action to recover the damages or equitable relief prescribed in subparagraph (A) may be maintained against any person in any Federal or State court of competent jurisdiction by any individual for and on behalf of\u2014\n**(i)**\nthe individual; or\n**(ii)**\nthe individual and other individuals similarly situated.\n**(C) Fees and costs**\nThe court in such an action shall, in addition to any judgment awarded to the plaintiff, allow a reasonable attorney's fee, reasonable expert witness fees, and other costs of the action to be paid by the defendant.\n**(D) Limitations**\nThe right provided by subparagraph (B) to bring an action by or on behalf of any individual shall terminate\u2014\n**(i)**\non the filing of a complaint by the Commissioner in an action under paragraph (5) in which restraint is sought of any further delay in the payment of the amount described in subparagraph (A)(I) to such individual by the person responsible under subparagraph (A) for the payment; or\n**(ii)**\non the filing of a complaint by the Commissioner in an action under paragraph (3) in which a recovery is sought of the damages described in subparagraph (A)(I) owing to an individual by a person liable under subparagraph (A),\nunless the action described in clause (i) or (ii) is dismissed without prejudice on motion of the Commissioner.\n**(3) Action by the Commissioner**\n**(A) Civil action**\nThe Commissioner may bring an action in any court of competent jurisdiction to recover the damages described in paragraph (2)(A)(I).\n**(B) Sums recovered**\nAny sums recovered by the Commissioner pursuant to subparagraph (A) shall be held in a special deposit account and shall be paid, on order of the Commissioner, directly to each individual affected. Any such sums not paid to an individual because of inability to do so within a period of 3 years shall be deposited into the Federal Family and Medical Leave Insurance Trust Fund.\n**(4) Limitation**\n**(A) In general**\nAn action may be brought under this subsection not later than 3 years after the date of the last event constituting the alleged violation for which the action is brought.\n**(B) Commencement**\nAn action brought by the Commissioner under this subsection shall be considered to be commenced on the date when the complaint is filed.\n**(5) Action for Injunction by Commissioner**\nThe district courts of the United States shall have jurisdiction, for cause shown, in an action brought by the Commissioner\u2014\n**(A)**\nto restrain violations of paragraph (1), including the restraint of any withholding of payment of wages, salary, employment benefits, or other compensation, plus interest, found by the court to be due to an individual; or\n**(B)**\nto award such other equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n##### (i) Applicability of certain Social Security Act provisions\nThe provisions of sections 204, 205, 206, and 208 of the Social Security Act shall apply to benefit payments authorized by and paid out pursuant to this section in the same way that such provisions apply to benefit payments authorized by and paid out pursuant to title II of such Act.\n##### (j) Effective date for applications\nApplications described in this section may be filed beginning 18 months after the date of enactment of this Act.\n#### 5. Funding for State administration option for legacy States\n##### (a) In general\n**(1) Payments to legacy States**\nIn each calendar year beginning with calendar year 2027, the Commissioner shall make a grant to each State that, for the calendar year preceding such calendar year, was a legacy State and that met the data sharing requirements of subsection (e), in an amount equal to the lesser of\u2014\n**(A)**\nan amount, as estimated by the Commissioner, equal to the total amount of comprehensive paid leave benefits that would have been paid under section 4 (including the costs to the Commissioner to administer such benefits, not to exceed (for purposes of estimating such total amount under this subparagraph) 7 percent of the total amount of such benefits paid) to individuals who received paid family and medical leave benefits under a State law described in paragraph (1) or (3) of subsection (b) during the calendar year preceding such calendar year if the State had not been a legacy State for such preceding calendar year; or\n**(B)**\nan amount equal to the total cost of paid family and medical leave benefits under a State law described in paragraph (1) or (3) of subsection (b) for the calendar year preceding such calendar year, including\u2014\n**(i)**\nany paid family and medical leave benefits provided by an employer (whether directly, under a contract with an insurer, or provided through a multiemployer plan) as described in subsection (d); and\n**(ii)**\nthe full cost to the State of administering such law (except that such cost may not exceed 7 percent of the total amount of paid family and medical leave benefits paid under such State law).\n**(2) Estimated payments**\nIn any case in which, during any calendar year, the Commissioner has reason to believe that a State will be a legacy State and meet the data sharing requirements of subsection (e) for such calendar year, the Commissioner may make estimated payments during such calendar year of the grant which would be paid to such State in the succeeding calendar year, to be adjusted as appropriate in the succeeding calendar year.\n##### (b) Legacy State\nFor purposes of this section, the term legacy State for a calendar year means a State with respect to which the Commissioner determines that\u2014\n**(1)**\nthe State has enacted, not later than the date of enactment of this Act, a State law that provides paid family and medical leave benefits;\n**(2)**\nfor any calendar year that begins before the date that is 3 years after the date of enactment of this Act, the State certifies to the Commissioner that the State intends to remain a legacy State and meet the data sharing requirements of subsection (e) at least through the first calendar year that begins on or after such date; and\n**(3)**\nfor any calendar year that begins on or after such date, a State law of the State provides for a State program to remain in effect throughout such calendar year that provides comprehensive paid family and medical leave benefits (which may be paid directly by the State or, if permitted under such State law, by an employer pursuant to such State law)\u2014\n**(A)**\nfor at least 12 full workweeks of leave during each 12-month period to at least all of those individuals in the State who would be eligible for comprehensive paid leave benefits under section 4 (without regard to section 2(5)(C)), except that the State shall provide such benefits for leave from employment by the State or any political subdivision thereof, and may elect to provide such benefits for leave from any other governmental employment; and\n**(B)**\nat a wage replacement rate that is at least equivalent to the wage replacement rate under the comprehensive paid leave benefit program under section 4 (without regard to section 2(5)(C)).\n##### (c) Covered employment under the law of a legacy State\nFor purposes of this Act, the term covered employment under the law of a legacy State means employment (or self-employment) with respect to which an individual would be eligible to receive paid family and medical benefits under the State law of a State, as described in paragraph (1) or (3) of subsection (b), during any period during which such State is a legacy State.\n##### (d) Employer-Provided benefits in a legacy State\n**(1) Treatment for purposes of this title**\nIn the case of a State that permits paid family and medical leave benefits to be provided by an employer (whether directly, under a contract with an insurer, or provided through a multiemployer plan) pursuant to a State law described in paragraph (1) or (3) of subsection (b)\u2014\n**(A)**\nsuch benefits shall be considered, for all purposes under this Act, paid family and medical leave benefits under the law of a legacy State; and\n**(B)**\nleave for which such benefits are paid shall be considered, for all such purposes, leave from covered employment under the law of a legacy State.\n**(2) Distribution of grant funds**\nIn any case in which paid family and medical leave benefits are provided by 1 or more employers (whether directly, under a contract with an insurer, or provided through a multiemployer plan) in a legacy State pursuant to a State law described in paragraph (1) or (3) of subsection (b), the State, upon the receipt of any grant amount under subsection (a), may distribute an appropriate share of such grant to each such employer.\n##### (e) Data sharing\nAs a condition of receiving a grant under subsection (a) in a calendar year, a State shall enter into an agreement with the Commissioner under which the State shall provide the Commissioner\u2014\n**(1)**\nwith information, to be provided periodically as determined by the Commissioner, concerning individuals who received a paid leave benefit under a State law described in paragraph (1) or (3) of subsection (b), including\u2014\n**(A)**\neach individual\u2019s name;\n**(B)**\ninformation to establish the individual\u2019s identity;\n**(C)**\ndates for which such paid leave benefits were paid;\n**(D)**\nthe amount of such paid leave benefit; and\n**(E)**\nto the extent available, such other information concerning such individuals as necessary for the purpose of carrying out this section and section 2(5)(C);\n**(2)**\nnot later than July 1 of such calendar year, the amount needed to adjust payments as described in subsection (a)(2) for the calendar year preceding such calendar year; and\n**(3)**\nsuch other information as needed to determine compliance with grant requirements.\n#### 6. Regulations\nThe Commissioner, in consultation with the Secretary of Labor, shall prescribe regulations necessary to carry out this Act. In developing such regulations, the Commissioner shall consider the input from a volunteer advisory body comprised of not more than 15 individuals, including experts in the relevant subject matter and officials charged with implementing State paid family and medical leave insurance programs. The Commissioner shall take such programs into account when proposing regulations. Such individuals shall be appointed as follows:\n**(1)**\nFive individuals to be appointed by the President.\n**(2)**\nThree individuals to be appointed by the majority leader of the Senate.\n**(3)**\nTwo individuals to be appointed by the minority leader of the Senate.\n**(4)**\nThree individuals to be appointed by the Speaker of the House of Representatives.\n**(5)**\nTwo individuals to be appointed by the minority leader of the House of Representatives.\n#### 7. GAO Study\n##### (a) Study\nAs soon as practicable after calendar year 2026, and every 5 years thereafter, the Comptroller General shall submit to Congress a report on family and medical leave insurance benefits paid under section 4 for any month during the covered period. The report shall include the following:\n**(1)**\nAn identification of the total number of applications for such benefits filed for any month during the covered period, and the average number of days occurring in the period beginning on the date on which such an application is received and ending on the date on which the initial determination of eligibility with respect to the application is made.\n**(2)**\nAn identification of the total number of requests for review of an initial adverse determination of eligibility for such benefits made during the covered period, and the average number of days occurring in the period beginning on the date on which such review is requested and ending on the date on which the final determination of eligibility with respect to such review is made.\n**(3)**\nAn identification of the total number of monthly benefit claim reports for such benefits filed during the covered period, and the average number of days occurring in the period beginning on the date on which such a claim report is received and ending on the date on which the initial determination of eligibility with respect to the claim report is made.\n**(4)**\nAn identification of the total number of requests for review of an initial adverse determination relating to a monthly benefit claim report for such benefits made during the covered period, and the average number of days occurring in the period beginning on the date on which such review is requested and ending on the date on which the final determination of eligibility with respect to such review is made.\n**(5)**\nAn identification of any excessive delay in any of the periods described in paragraphs (1) through (4), including\u2014\n**(A)**\na description of the causes for such delay;\n**(B)**\ninformation any correlation in such delay to claimant demographics, industry sector, or qualifying reason.\n**(6)**\nAn identification of any additional data that needs to be collected as part of the application process for benefits to produce the report required under this section.\n##### (b) Covered period\nIn this section, the term covered period means\u2014\n**(1)**\nwith respect to the report due as soon as practicable after calendar year 2026, such calendar year; and\n**(2)**\nwith respect to the report due every 5 years thereafter, the 5-calendar year period ending on December 31 of the year prior to the year in which such report is due.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-09-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5390",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAMILY Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-17T18:31:53Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2823is.xml"
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
      "title": "FAMILY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAMILY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Family and Medical Insurance Leave Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide paid family and medical leave benefits to certain individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:16Z"
    }
  ]
}
```
