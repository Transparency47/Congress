# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3752
- Title: SAVE America Act
- Congress: 119
- Bill type: S
- Bill number: 3752
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-15T18:20:19Z
- Update date including text: 2026-04-15T18:20:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3752",
    "number": "3752",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SAVE America Act",
    "type": "S",
    "updateDate": "2026-04-15T18:20:19Z",
    "updateDateIncludingText": "2026-04-15T18:20:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-30T03:41:37Z",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "FL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "FL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "ID"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "OK"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "SC"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "ID"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MO"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "WY"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "SD"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "ND"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "OK"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WV"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WY"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "OH"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AR"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "KY"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "LA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "LA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "UT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "MS"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "SD"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "SC"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3752is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3752\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Lee (for himself, Mr. Scott of Florida , Mr. Budd , Mr. Banks , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the National Voter Registration Act of 1993 to require proof of United States citizenship to register an individual to vote in elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguard American Voter Eligibility Act or the SAVE America Act .\n#### 2. Ensuring only citizens are registered to vote in elections for Federal office\n##### (a) Definition of documentary proof of United States citizenship\nSection 3 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20502 ) is amended\u2014\n**(1)**\nby striking As used and inserting (a) In general .\u2014As used ; and\n**(2)**\nby adding at the end the following:\n(b) Documentary proof of United States citizenship As used in this Act, the term documentary proof of United States citizenship means, with respect to an applicant for voter registration, any of the following: (1) A form of identification issued consistent with the requirements of the REAL ID Act of 2005 that indicates the applicant is a citizen of the United States. (2) A valid United States passport. (3) The applicant's official United States military identification card, together with a United States military record of service showing that the applicant's place of birth was in the United States. (4) A valid government-issued photo identification card issued by a Federal, State or Tribal government showing that the applicant\u2019s place of birth was in the United States. (5) A valid government-issued photo identification card issued by a Federal, State or Tribal government other than an identification described in paragraphs (1) through (4), but only if presented together with one or more of the following: (A) A certified birth certificate issued by a State, a unit of local government in a State, or a Tribal government which\u2014 (i) was issued by the State, unit of local government, or Tribal government in which the applicant was born; (ii) was filed with the office responsible for keeping vital records in the State; (iii) includes the full name, date of birth, and place of birth of the applicant; (iv) lists the full names of one or both of the parents of the applicant; (v) has the signature of an individual who is authorized to sign birth certificates on behalf of the State, unit of local government, or Tribal government in which the applicant was born; (vi) includes the date that the certificate was filed with the office responsible for keeping vital records in the State; and (vii) has the seal of the State, unit of local government, or Tribal government that issued the birth certificate. (B) An extract from a United States hospital Record of Birth created at the time of the applicant's birth which indicates that the applicant\u2019s place of birth was in the United States. (C) A final adoption decree showing the applicant\u2019s name and that the applicant\u2019s place of birth was in the United States. (D) A Consular Report of Birth Abroad of a citizen of the United States or a certification of the applicant\u2019s Report of Birth of a United States citizen issued by the Secretary of State. (E) A Naturalization Certificate or Certificate of Citizenship issued by the Secretary of Homeland Security or any other document or method of proof of United States citizenship issued by the Federal Government pursuant to the Immigration and Nationality Act. (F) An American Indian Card issued by the Department of Homeland Security with the classification \u2018KIC\u2019. .\n##### (b) Application of requirements\nSection 4 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503 ) is amended by striking subsection (b) and inserting the following:\n(b) Requiring applicants To present documentary proof of United States citizenship Under any method of voter registration in a State, the State shall not accept and process an application to register to vote in an election for Federal office unless the applicant presents documentary proof of United States citizenship with the application. .\n##### (c) Registration with application for motor vehicle driver\u2019s license\nSection 5 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20504 ) is amended\u2014\n**(1)**\nin subsection (a)(1), by striking Each State motor vehicle driver's license application and inserting Subject to the requirements under section 8(j), each State motor vehicle driver's license application ;\n**(2)**\nin subsection (c)(1), by striking Each State shall include and inserting Subject to the requirements under section 8(j), each State shall include ;\n**(3)**\nin subsection (c)(2)(B)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by adding and at the end; and\n**(C)**\nby adding at the end the following new clause:\n(iii) verify that the applicant is a citizen of the United States; ;\n**(4)**\nin subsection (c)(2)(C)(i), by striking (including citizenship) and inserting , including the requirement that the applicant provides documentary proof of United States citizenship ; and\n**(5)**\nin subsection (c)(2)(D)(iii), by striking ; and and inserting the following: , other than as evidence in a criminal proceeding or immigration proceeding brought against an applicant who knowingly attempts to register to vote and knowingly makes a false declaration under penalty of perjury that the applicant meets the eligibility requirements to register to vote in an election for Federal office; and .\n##### (d) Requiring documentary proof of United States citizenship with national mail voter registration form\nSection 6 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20505 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby striking Each State shall accept and use and inserting Subject to the requirements under section 8(j), each State shall accept and use ; and\n**(B)**\nby striking Federal Election Commission and inserting Election Assistance Commission ;\n**(2)**\nin subsection (b), by adding at the end the following: The chief State election official of a State shall take such steps as may be necessary to ensure that residents of the State are aware of the requirement to provide documentary proof of United States citizenship to register to vote in elections for Federal office in the State. ;\n**(3)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking and at the end;\n**(B)**\nin subparagraph (B) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(C) the person did not provide documentary proof of United States citizenship when registering to vote. ; and\n**(4)**\nby adding at the end the following new subsection:\n(e) Ensuring proof of United States citizenship (1) Presenting proof of United States citizenship to election official An applicant who submits the mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a) shall not be registered to vote in an election for Federal office unless\u2014 (A) the applicant presents documentary proof of United States citizenship in person to the office of the appropriate election official not later than the deadline provided by State law for the receipt of a completed voter registration application for the election; or (B) in the case of a State which permits an individual to register to vote in an election for Federal office at a polling place on the day of the election and on any day when voting, including early voting, is permitted for the election, the applicant presents documentary proof of United States citizenship to the appropriate election official at the polling place not later than the date of the election. (2) Notification of requirement Upon receiving an otherwise completed mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a), the appropriate election official shall transmit a notice to the applicant of the requirement to present documentary proof of United States citizenship under this subsection, and shall include in the notice instructions to enable the applicant to meet the requirement. (3) Accessibility Each State shall, in consultation with the Election Assistance Commission, ensure that reasonable accommodations are made to allow an individual with a disability who submits the mail voter registration application form prescribed by the Election Assistance Commission pursuant to section 9(a)(2) or a form described in paragraph (1) or (2) of subsection (a) to present documentary proof of United States citizenship to the appropriate election official. .\n##### (e) Requirements for voter registration agencies\nSection 7 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20506 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (4)(A), by adding at the end the following new clause:\n(iv) Receipt of documentary proof of United States citizenship of each applicant to register to vote in elections for Federal office in the State. ; and\n**(B)**\nin paragraph (6)\u2014\n**(i)**\nin subparagraph (A)(i)(I), by striking (including citizenship) and inserting , including the requirement that the applicant provides documentary proof of United States citizenship ;\n**(ii)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively; and\n**(iii)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) ask the applicant the question, Are you a citizen of the United States? and if the applicant answers in the affirmative require documentary proof of United States citizenship prior to providing the form under subparagraph (C); ; and\n**(2)**\nin subsection (c)(1), by inserting who are citizens of the United States after for persons .\n##### (f) Requirements with respect to administration of voter registration\nSection 8 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking In the administration of voter registration and inserting Subject to the requirements of subsection (j), in the administration of voter registration ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (B), by striking or at the end; and\n**(ii)**\nby adding at the end the following new subparagraphs:\n(D) based on documentary proof or verified information that the registrant is not a United States citizen; or (E) the registration otherwise fails to comply with applicable State law; ;\n**(2)**\nby redesignating subsection (j) as subsection (l); and\n**(3)**\nby inserting after subsection (i) the following new subsections:\n(j) Ensuring only citizens are registered To vote (1) In general Notwithstanding any other provision of this Act, a State may not register an individual to vote in elections for Federal office held in the State unless, at the time the individual applies to register to vote, the individual provides documentary proof of United States citizenship. (2) Additional processes in certain cases (A) Process for those without documentary proof (i) In general Subject to any relevant guidance adopted by the Election Assistance Commission, each State shall establish a process under which an applicant who cannot provide documentary proof of United States citizenship under paragraph (1) may, if the applicant signs an attestation under penalty of perjury that the applicant is a citizen of the United States and eligible to vote in elections for Federal office, submit such other evidence to the appropriate State or local official demonstrating that the applicant is a citizen of the United States and such official shall make a determination as to whether the applicant has sufficiently established United States citizenship for purposes of registering to vote in elections for Federal office in the State. (ii) Affidavit requirement If a State or local official makes a determination under clause (i) that an applicant has sufficiently established United States citizenship for purposes of registering to vote in elections for Federal office in the State, such determination shall be accompanied by an affidavit developed under clause (iii) signed by the official swearing or affirming the applicant sufficiently established United States citizenship for purposes of registering to vote. (iii) Development of affidavit by the Election Assistance Commission The Election Assistance Commission shall develop a uniform affidavit for use by State and local officials under clause (ii), which shall\u2014 (I) include an explanation of the minimum standards required for a State or local official to register an applicant who cannot provide documentary proof of United States citizenship to vote in elections for Federal office in the State; and (II) require the official to explain the basis for registering such applicant to vote in such elections. (B) Process in case of certain discrepancies in documentation Subject to any relevant guidance adopted by the Election Assistance Commission, each State shall establish a process under which an applicant can provide such additional documentation to the appropriate election official of the State as may be necessary to establish that the applicant is a citizen of the United States in the event of a discrepancy with respect to the applicant\u2019s documentary proof of United States citizenship. (3) State requirements Each State shall take affirmative steps on an ongoing basis to ensure that only United States citizens are registered to vote under the provisions of this Act, which shall include the establishment of a program described in paragraph (4) not later than 30 days after the date of the enactment of this subsection. (4) Program described A State may meet the requirements of paragraph (3) by establishing a program under which the State identifies individuals who are not United States citizens using information supplied by one or more of the following sources: (A) The Department of Homeland Security through the Systematic Alien Verification for Entitlements ( SAVE ) or otherwise. (B) The Social Security Administration through the Social Security Number Verification Service, or otherwise. (C) State agencies that supply State identification cards or driver\u2019s licenses where the agency confirms the United States citizenship status of applicants. (D) Other sources, including databases, which provide confirmation of United States citizenship status. (5) Availability of information (A) In general At the request of a State election official (including a request related to a process established by a State under paragraph (2)(A) or (2)(B)), any head of a Federal department or agency possessing information relevant to determining the eligibility of an individual to vote in elections for Federal office shall, not later than 24 hours after receipt of such request, provide the official with such information as may be necessary to enable the official to verify that an applicant for voter registration in elections for Federal office held in the State or a registrant on the official list of eligible voters in elections for Federal office held in the State is a citizen of the United States, which shall include providing the official with such batched information as may be requested by the official. (B) Use of SAVE system The Secretary of Homeland Security may respond to a request received under paragraph (1) by using the system for the verification of immigration status under the applicable provisions of section 1137 of the Social Security Act ( 42 U.S.C. 1320b\u20137 ), as established pursuant to section 121(c) of the Immigration Reform and Control Act of 1986 ( Public Law 99\u2013603 ). (C) Sharing of information The heads of Federal departments and agencies shall share information with each other with respect to an individual who is the subject of a request received under paragraph (A) in order to enable them to respond to the request. (D) Investigation for purposes of removal The Secretary of Homeland Security shall conduct an investigation to determine whether to initiate removal proceedings under section 239 of the Immigration and Nationality Act ( 8 U.S.C. 1229 ) if it is determined pursuant to subparagraph (A) or (B) that an alien (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) is unlawfully registered to vote in elections for Federal office. (E) Prohibiting fees The head of a Federal department or agency may not charge a fee for responding to a State\u2019s request under paragraph (A). (k) Removal of noncitizens from registration rolls A State shall remove an individual who is not a citizen of the United States from the official list of eligible voters for elections for Federal office held in the State at any time upon receipt of documentation or verified information that a registrant is not a United States citizen. .\n##### (g) Clarification of authority of State To remove noncitizens from official list of eligible voters\n**(1) In general**\nSection 8(a)(4) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507(a)(4) ) is amended\u2014\n**(A)**\nby striking or at the end of subparagraph (A);\n**(B)**\nby adding or at the end of subparagraph (B); and\n**(C)**\nby adding at the end the following new subparagraph:\n(C) documentary proof or verified information that the registrant is not a United States citizen; .\n**(2) Conforming amendment**\nSection 8(c)(2)(B)(i) of such Act ( 52 U.S.C. 20507(c)(2)(B)(i) ) is amended by striking (4)(A) and inserting (4)(A) or (C) .\n##### (h) Requirements with respect to Federal mail voter registration form\n**(1) Contents of mail voter registration form**\nSection 9(b) of such Act ( 52 U.S.C. 20508(b) ) is amended\u2014\n**(A)**\nin paragraph (2)(A), by striking (including citizenship) and inserting (including an explanation of what is required to present documentary proof of United States citizenship) ;\n**(B)**\nin paragraph (3), by striking and at the end;\n**(C)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following new paragraph:\n(5) shall include a section, for use only by a State or local election official, to record the type of document the applicant presented as documentary proof of United States citizenship, including the date of issuance, the date of expiration (if any), the office which issued the document, and any unique identification number associated with the document. .\n**(2) Information on mail voter registration form**\nSection 9(b)(4) of such Act ( 52 U.S.C. 20508(b)(4) ) is amended\u2014\n**(A)**\nby redesignating clauses (i) through (iii) as subparagraphs (A) through (C), respectively; and\n**(B)**\nin subparagraph (C) (as so redesignated and as amended by paragraph (1)(C)), by striking ; and and inserting the following: , other than as evidence in a criminal proceeding or immigration proceeding brought against an applicant who attempts to register to vote and makes a false declaration under penalty of perjury that the applicant meets the eligibility requirements to register to vote in an election for Federal office; and .\n##### (i) Private right of action\nSection 11(b)(1) of the National Voter Registration Act of 1993 ( 52 U.S.C. 20510(b)(1) ) is amended by striking a violation of this Act and inserting a violation of this Act, including the act of an election official who registers an applicant to vote in an election for Federal office who fails to present documentary proof of United States citizenship, .\n##### (j) Criminal penalties\nSection 12(2) of such Act ( 52 U.S.C. 20511(2) ) is amended\u2014\n**(1)**\nby striking or at the end of subparagraph (A);\n**(2)**\nby redesignating subparagraph (B) as subparagraph (D); and\n**(3)**\nby inserting after subparagraph (A) the following new subparagraphs:\n(B) in the case of an officer or employee of the executive branch, providing material assistance to a noncitizen in attempting to register to vote or vote in an election for Federal office; (C) registering an applicant to vote in an election for Federal office who fails to present documentary proof of United States citizenship; or .\n##### (k) Special rule for States not requiring voter registration\nSection 4 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20503 ), as amended by subsection (b), is amended by adding at the end the following:\n(c) Special rule for States not requiring voter registration In the case of a State or jurisdiction that does not require voter registration as a requirement to vote in an election for Federal office on or after the date of the enactment of this subsection, the State or jurisdiction shall be deemed to meet the requirements of this Act if the State or jurisdiction establishes a system for confirming the citizenship of individuals voting in an election for Federal office prior to the first day for voting with respect to such election and provides such confirmation of citizenship status for each eligible voter to election officials at the polling places during the voting period. .\n##### (l) Election Assistance Commission guidance\nNot later than 10 days after the date of the enactment of this Act, the Election Assistance Commission shall adopt and transmit to the chief State election official of each State guidance with respect to the implementation of the requirements under the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ), as amended by this section.\n##### (m) Inapplicability of Paperwork Reduction Act\nSubchapter I of chapter 35 of title 44 (commonly referred to as the Paperwork Reduction Act ) shall not apply with respect to the development or modification of voter registration materials under the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ), as amended by this section, including the development or modification of any voter registration application forms.\n##### (n) Duty of Secretary of Homeland Security To notify election officials of naturalization\nUpon receiving information that an individual has become a naturalized citizen of the United States, the Secretary of Homeland Security shall promptly provide notice of such information to the appropriate chief election official of the State in which such individual is domiciled.\n##### (o) Rule of construction regarding provisional ballots\nNothing in this section or in any amendment made by this section may be construed to supercede, restrict, or otherwise affect the ability of an individual to cast a provisional ballot in an election for Federal office or to have the ballot counted in the election if the individual is verified as a citizen of the United States pursuant to section 8(j) of the National Voter Registration Act of 1993 (as added by subsection (f)).\n##### (p) Rule of construction regarding effect on State exemptions from other Federal laws\nNothing in this section or in any amendment made by this section may be construed to affect the exemption of a State from any requirement of any Federal law other than the National Voter Registration Act of 1993 ( 52 U.S.C. 20501 et seq. ).\n##### (q) Effective date\nThis section and the amendments made by this section shall take effect on the date of the enactment of this section, and shall apply with respect to applications for voter registration which are submitted on or after such date.\n#### 3. Photo voter identification required for voting in a Federal election\n##### (a) In general\nEach individual voting in an election for Federal office shall present an eligible photo identification document.\n##### (b) Presentation requirements\n**(1) In-person voting**\nIn the case of an individual who votes in-person, the eligible photo identification document shall\u2014\n**(A)**\nbe a tangible (not digital) document; and\n**(B)**\nbe presented at the time of voting.\n**(2) Absentee voting**\nIn the case of an individual voting by absentee ballot, the individual shall include a copy of the eligible photo identification document\u2014\n**(A)**\nwith the request for an absentee ballot; and\n**(B)**\nwith the submission of the absentee ballot.\n##### (c) Eligible photo identification document\nFor purposes of this section:\n**(1) In general**\nThe term eligible photo identification document means any document which\u2014\n**(A)**\nis issued by an authority described in paragraph (2); and\n**(B)**\nmeets the requirements of paragraph (3).\n**(2) Issuing authority**\nThe following are authorities described in this paragraph:\n**(A)**\nA State agency responsible for issuing State motor vehicle drivers' licenses.\n**(B)**\nA State or local election office.\n**(C)**\nA Native tribal government.\n**(D)**\nThe Department of State.\n**(E)**\nThe Department of War.\n**(F)**\nA branch of the Armed Forces.\n**(3) Requirements**\nA document meets the requirements of this paragraph if the document contains\u2014\n**(A)**\na photograph of the individual identified on the document;\n**(B)**\nan indication on the front of the document that the individual identified on the document is a United States citizen; and\n**(C)**\neither\u2014\n**(i)**\nan identification number issues by the entity described in paragraph (2)(A); or\n**(ii)**\nthe last four digits of the social security number of the individual identified on the document.\n**(4) Use of additional documentation**\n**(A) Use of additional documentation**\nA document which fails to meet the requirements of paragraph (3)(B) shall not fail to be treated as an eligible photo identification document if the document is presented together with another identification document that indicates the individual is a United States citizen.\n**(B) States using SAVE system**\n**(i) In general**\nThe requirements of paragraph (3)(B) shall not apply to an individual\u2014\n**(I)**\nwho votes in a State or jurisdiction which meets the requirements of clause (ii); and\n**(II)**\nwho registered to vote in such State or jurisdiction before the most recent date on which the State or jurisdiction last submitted its voter registration rolls to the Department of Homeland Security as provided in clause (ii)(I).\n**(ii) Requirements**\nThe requirements of this clause are met if\u2014\n**(I)**\nthe State or jurisdiction has submitted its voter registration list to the Department of Homeland Security through the Systematic Alien Verification for Entitlements (SAVE) program not less frequently than quarterly since June 1, 2025, for purposes of identifying ineligible registrations and non-citizens; and\n**(II)**\nthe State or jurisdiction indicates in each voter record on its voter rolls whether the voter has been verified as a United States citizen based on the information provided by the Department of Homeland Security under subclause (I), and the date of such verification.\n**(iii) Special rule for States not requiring voter registration**\nIn the case of a State or jurisdiction that does not require voter registration as a requirement to vote in an election for Federal office on or after the date of the enactment of this Act\u2014\n**(I)**\nclause (i)(ii) shall not apply; and\n**(II)**\nthe State or jurisdiction shall be deemed to meet the requirements of clause (ii) if the State or jurisdiction establishes a system for confirming the citizenship of individuals voting in an election for Federal office prior to the first day of the period described in section 3 with respect to such election and provides such confirmation of citizenship status for each eligible voter to election officials at the polling places during the voting period.\n##### (d) Conforming amendment\nSection 303(b) of the Help America Vote Act of 2002 ( 52 U.S.C. 21083(b) ) is amended by striking all that precedes paragraph (4).\n##### (e) Effective date\nEach State and jurisdiction shall be required to comply with the requirements of this section with respect to all elections for Federal office occurring on and after the date of the enactment of this section.",
      "versionDate": "2026-01-29",
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
        "actionDate": "2026-01-30",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "7296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAVE America Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-10",
        "text": "Received in the Senate."
      },
      "number": "22",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "128",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-06",
        "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Homeland Security and Further Additional Continuing Appropriations Act, 2026",
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
        "updateDate": "2026-02-23T23:35:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-29",
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
          "measure-id": "id119s3752",
          "measure-number": "3752",
          "measure-type": "s",
          "orig-publish-date": "2026-01-29",
          "originChamber": "SENATE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3752v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2026-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>"
        },
        "title": "SAVE America Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3752.xml",
    "summary": {
      "actionDate": "2026-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s3752"
    },
    "title": "SAVE America Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguard American Voter Eligibility Act or the SAVE America Act</strong></p><p>This bill requires individuals to provide documentary proof of U.S. citizenship when registering to vote, and requires photo identification to vote,\u00a0in federal elections.</p><p>Specifically, the bill prohibits states from accepting and processing an application to register to vote in a federal election unless the applicant presents documentary proof of U.S. citizenship.\u00a0The bill specifies what documents are considered acceptable proof of U.S. citizenship, such as\u00a0identification that complies with the REAL ID Act of 2005 that indicates U.S. citizenship.</p><p>Further, the bill (1) prohibits states from registering an individual to vote in a federal election unless, at the time the individual applies to register to vote, the individual provides documentary proof of U.S. citizenship; and (2) requires states to establish an alternative process to demonstrate U.S. citizenship.</p><p>Each state must take affirmative steps on an ongoing basis to ensure that only U.S. citizens are registered to vote, which shall include establishing a program to identify individuals who are not U.S. citizens using information supplied by certain sources.</p><p>Additionally, states must remove noncitizens from their official lists of eligible voters.</p><p>The bill (1) provides\u00a0for a private right of action for certain violations, and (2) establishes criminal penalties for certain offenses.</p><p>Individuals voting in federal elections must present an eligible photo identification document. An individual who votes by absentee ballot must submit a copy of their identification document with both the request for, and the submission of, the absentee ballot.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s3752"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3752is.xml"
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
      "title": "SAVE America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAVE America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguard American Voter Eligibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Voter Registration Act of 1993 to require proof of United States citizenship to register an individual to vote in elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:24Z"
    }
  ]
}
```
