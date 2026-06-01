# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4911?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4911
- Title: POLL Act
- Congress: 119
- Bill type: HR
- Bill number: 4911
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-03-31T19:22:20Z
- Update date including text: 2026-03-31T19:22:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4911",
    "number": "4911",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "POLL Act",
    "type": "HR",
    "updateDate": "2026-03-31T19:22:20Z",
    "updateDateIncludingText": "2026-03-31T19:22:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:03:20Z",
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
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "AZ"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OH"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IN"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "FL"
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
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "AL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "VA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MD"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
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
      "sponsorshipDate": "2025-08-05",
      "state": "DC"
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OR"
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
      "sponsorshipDate": "2025-08-05",
      "state": "IL"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "VA"
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
      "sponsorshipDate": "2025-08-05",
      "state": "AL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "OH"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MI"
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
      "sponsorshipDate": "2025-08-05",
      "state": "MS"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4911ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4911\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Williams of Georgia (for herself, Ms. Crockett , Ms. Ansari , Ms. Brown , Mr. Carson , Mrs. Cherfilus-McCormick , Ms. Clarke of New York , Ms. DelBene , Mr. Deluzio , Mr. Doggett , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Figures , Mr. Garc\u00eda of Illinois , Mr. Green of Texas , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kamlager-Dove , Mr. Krishnamoorthi , Ms. Lee of Pennsylvania , Mr. Lynch , Ms. McClellan , Mrs. McIver , Mr. Meeks , Mr. Mfume , Mr. Mullin , Ms. Norton , Mrs. Ramirez , Ms. Salinas , Ms. Schakowsky , Mr. Scott of Virginia , Ms. Sewell , Ms. Simon , Ms. Strickland , Mrs. Sykes , Mr. Thanedar , Mr. Thompson of Mississippi , Ms. Tlaib , and Mr. Tonko ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to ensure that voters in elections for Federal office do not wait in long lines in order to vote, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the People Over Long Lines Act or the POLL Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe right to vote for all Americans is fundamental and rules for voting and election administration should protect the right to vote and promote voter participation.\n**(2)**\nIt is the responsibility of the State and Federal Governments to ensure that every eligible citizen is able to register to vote and to cast a ballot.\n**(3)**\nThere continues to be an alarming movement to erect barriers to make it more difficult for Americans to participate in our Nation\u2019s democratic process. The Nation has witnessed unprecedented efforts to turn back the clock and erect barriers to voting for communities of color, which have faced historic and continuing discrimination, as well as disabled, young, elderly, and low-income Americans.\n**(4)**\nOne way voting in communities of color has been suppressed is through long waits at polling locations. Studies have shown a number of contributing factors, including the drastic reduction of early voting days, poor allocation of resources to certain communities, cuts to election funding, and a reduction of polling locations.\n**(5)**\nA 2019 study led by economist Keith Chen of the University of California, Los Angeles, matched anonymous location data from 10,000,000 smart phones to 93,000 polling places to create the most extensive map to date of voter wait times across the United States. The results showed one very clear disparity: voters in predominantly Black neighborhoods waited 29 percent longer, on average, than those in White neighborhoods. They were also about 74 percent more likely to wait for more than half an hour.\n**(6)**\nWaiting in long lines discourages people from voting, undermines confidence in the electoral system, and imposes economic costs on voters.\n**(7)**\nLong lines are estimated to have deterred between 500,000 and 700,000 people from casting their ballot in 2012.\n**(8)**\nThese problems led to the creation of the bipartisan Presidential Commission on Election Administration, which issued a 2014 report that set forth a standard: No citizen should have to wait more than 30 minutes to vote. .\n**(9)**\nDespite the work of the Presidential Commission on Election Administration, long lines continue, particularly in communities of color where racial discrimination in voting is a clear and persistent problem.\n**(10)**\nIn the Arizona 2016 Presidential primary, in one Maricopa County polling place for mostly Latino voters, some waited for 4 hours or more in the 80-degree heat to cast their ballots. For the 2016 general election, 3 people collapsed while waiting to vote in an hours-long line in Georgia, and a line to vote in Ohio was a half-mile long.\n**(11)**\nAccording to a nationwide study, in 2016, roughly 3 percent of people standing in line at voting locations left before they could vote as a result of long lines.\n**(12)**\nThe disenfranchisement that long lines create for voters is not limited to that one election. Research suggests that for each hour would-be voters wait, their probability of voting in the next election drops by 1 percentage point.\n**(13)**\nCongress has the authority under article I, section 4 of the Constitution of the United States to enact laws governing the time, place, and manner of Federal elections.\n**(14)**\nCongress also has authority under section 2 of the 15th Amendment to enforce the right of citizens of the United States to vote, which shall not be denied or abridged by the United States, by legislation.\n#### 3. Preventing unreasonable voter waiting times\n##### (a) State plans required\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 20901 et seq. ), as amended by section 2(a) of the COCOA Act of 2024, is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Unreasonable voter waiting times (a) State plans (1) In general Not later than 60 days before each election for Federal office, each State shall make public (including through the website of the State on which election information is normally published) and submit to the Commission a written plan which meets the public notice and comment requirements of paragraph (2) and describes the measures it is implementing to ensure, to the greatest extent possible, an equitable waiting time for all voters in the State, including for voters with disabilities, and a waiting time of less than 30 minutes at any polling place in the election. (2) Public notice comment requirement The public notice and comment requirements of this paragraph are met if\u2014 (A) not later than 30 days prior to the submission of the plan to the Commission, the State made a preliminary version of the plan available for public inspection and comment; (B) the State publishes notice that the preliminary version of the plan is so available; and (C) the State took the public comments made regarding the preliminary version of the plan into account in preparing the plan which was submitted to the Commission under paragraph (1). (b) Prohibition on unreasonable voter waiting times Each State shall ensure that no person voting in an election for Federal office shall wait for more than 30 minutes at any polling place for purposes of casting a vote in such election. (c) Remedial plans for states with excessive voter wait times (1) Review of voter wait times After each election for Federal office, the Commission shall review voter waiting times for each jurisdiction for which voting in such election took place and make publicly available a report on its findings. (2) State remedial plans (A) Remedial plans Notwithstanding section 209, each jurisdiction for which the Commission, after the review conducted under paragraph (1), determines that a substantial number of voters, including voters with disabilities, waited more than 60 minutes to cast a vote, or in which there were substantial violations of the standards established under section 299, shall comply with a State remedial plan established by the Attorney General to provide for the effective allocation of resources to administer elections for Federal office held in the State and to reduce the waiting time of voters. (B) Coordination Each remedial plan established by the Attorney General shall provide for coordination between the Commission, the Attorney General, and the State involved to monitor the compliance of the State with the remedial plan during the period leading up to the election and on the date of the election and to respond to serious delays in the ability of voters, including voters with disabilities, to cast their ballots at polling places. (C) Termination A jurisdiction shall not be required to comply with a State remedial plan required under subparagraph (A) if the Commission determines that the voter waiting times were less than 60 minutes for 2 consecutive regularly scheduled general elections for Federal office. (3) Jurisdiction defined For purposes of this subsection, the term jurisdiction has the meaning given the term registrar's jurisdiction in section 8(j) of the National Voter Registration Act of 1993 ( 42 U.S.C. 1973gg\u20136(j) ). (4) Standards Not later than 180 days after the date of the enactment of this section, the Attorney General shall establish standards for conducting the review under paragraph (1) and for establishing remedial plans under paragraph (2)(A). (5) Role of Office of Civil Rights and Commission The Attorney General shall carry out this section acting through the Assistant Attorney General for the Civil Rights Division of the Department of Justice and in consultation with the Commission. (6) Appropriations In addition to other amounts authorized to be appropriated to the Commission, there are authorized to be appropriated for each of the fiscal years 2025 through 2034, $5,000,000 for each such year for the Commission to carry out this subsection. (d) Emergency ballots (1) In general In the event of a failure of voting equipment or other circumstance at a polling place that causes an unreasonable delay, any individual who is waiting at the polling place to cast a ballot in an election for Federal office at the time of the failure shall be advised immediately of the individual's right to use an emergency paper ballot, and upon request shall be provided with such an emergency paper ballot for the election and the supplies necessary to mark the ballot. (2) Ballot requirements Any emergency paper ballot provided under paragraph (1) shall\u2014 (A) include the names of each candidate for each Federal office for which voting occurs at such polling place; and (B) be available in each language for which other ballots provided at the polling place are available. (3) Disposition of ballot Any emergency paper ballot which is cast by an individual under this subsection shall be counted in the same manner as a regular ballot, unless the individual casting the ballot would have otherwise been required to cast a provisional ballot in the absence of the delay, in which case that ballot shall be treated in the same manner as a provisional ballot. .\n##### (b) Private right of action\nTitle IV of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 et seq. ) is amended by adding at the end the following new section:\n403. Private right of action for unreasonable voter waiting time (a) In general In the case of a violation of section 305(b), section 402 shall not apply and any person who is aggrieved by such violation may commence a civil action in any appropriate district court of the United States for relief. (b) Relief In any civil action commenced under subsection (a): (1) In general If the court finds a violation of section 305(b), the court shall assess a civil penalty equal to the sum of\u2014 (A) $50; plus (B) an additional $50 for each additional hour the person waited at the polling place to cast a vote; plus (C) reasonable attorney fees, including litigation expenses, and costs. (2) Special rule If the court determines that the violation was due to an intentional action to suppress votes or was made with reckless disregard of the requirements of section 305\u2014 (A) paragraph (1)(A) shall be applied by substituting $650 for $50 ; and (B) paragraph (1)(B) shall be applied by substituting $150 for $50 . .\n##### (c) Conforming amendment\nSection 202 of such Act ( 52 U.S.C. 20922 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (5) and (6) as paragraphs (6) and (7), respectively; and\n**(2)**\nby inserting after paragraph (4) the following new paragraph:\n(5) carrying out the duties described in section 305(c); .\n##### (d) Clerical amendments\nThe table of contents of the Help America Vote Act of 2002 is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to sections 306 and 307, and by inserting after the item relating to section 304 the following new item:\nSec. 305. Unreasonable voter waiting times. ;\nand\n**(2)**\nby inserting after the item relating to section 402 the following new item:\nSec. 403. Private right of action for unreasonable voter waiting time. .\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to elections held on or after the expiration of the 180-day period which begins on the date of the enactment of this Act.\n#### 4. Minimum required voting systems, poll workers, and election resources\n##### (a) Minimum Requirements\n**(1) In general**\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended by adding at the end the following new subtitle:\nC Additional requirements 321. Minimum required voting systems and poll workers (a) In General Each State shall provide for the minimum required number of voting systems, poll workers, and other election resources (including all other physical resources) for each voting site on the day of any Federal election and on any days during which such State allows early voting for a Federal election in accordance with the standards determined under section 299. (b) Definitions For purposes of this section and section 299\u2014 (1) the term voting site means a polling location; and (2) the term voting system means the total combination of mechanical, electromechanical, or electronic equipment (including the software, firmware, and documentation required to program, control, and support the equipment) that is used at a voting site\u2014 (A) to check the official list of eligible voters for purposes of confirming that an individual is eligible to cast a vote at the site; (B) to cast and count votes; and (C) to maintain and produce any audit trail information. (c) Effective date Each State shall be required to comply with the requirements of this section on and after January 1, 2027. .\n**(2) Conforming amendment**\nSection 401 of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 ) is amended by striking and 303 and inserting 303, and subtitle C .\n**(3) Clerical amendment**\nThe table of contents of such Act is amended by adding at the end of the items relating to title III the following:\nSubtitle C\u2014Additional Requirements Sec. 321. Minimum required voting systems and poll workers. .\n##### (b) Standards\n**(1) In general**\nTitle II of the Help America Vote Act of 2002 ( 52 U.S.C. 20921 et seq. ) is amended by adding at the end the following new subtitle:\nE Guidance and standards 299. Standards for establishing the minimum required voting systems and poll workers (a) In General Not later than 6 months after the date of the enactment of the POLL Act, the Attorney General, acting through the Assistant Attorney General for the Civil Rights Division of the Department of Justice and in consultation with the Commission, shall issue standards regarding the minimum number of voting systems, poll workers, and other election resources (including all other physical resources) required under section 321 on the day of any Federal election and on any days during which early voting is allowed for a Federal election. (b) Distribution (1) In general The standards described in subsection (a) shall provide for a uniform and nondiscriminatory distribution of such systems, workers, and other resources, and shall take into account, among other factors, the following with respect to any voting site (as defined in section 321(b)): (A) The voting-age population. (B) Voter turnout in past elections. (C) The number of voters registered. (D) The number of voters who have registered since the most recent Federal election. (E) Census data for the population served by such voting site. (F) The educational levels and socio-economic factors of the population served by such voting site. (G) The needs and numbers of disabled voters and voters with limited English proficiency. (H) The type of voting systems used. (2) No factor dispositive The standards shall provide that any distribution of such systems shall take into account the totality of all relevant factors, including the effects of State laws on the availability of such systems and resources for use by local election officials, and no single factor shall be dispositive under the standards. (3) Purpose To the extent possible, the standards shall provide for a distribution of voting systems, poll workers, and other election resources, with the goals of\u2014 (A) ensuring an equal waiting time for all voters in the State; and (B) preventing a waiting time of over 30 minutes at any polling place. (4) Special rule regarding electronic poll books Notwithstanding paragraphs (1), (2), and (3), in the case of any voting site that uses an electronic poll book, the standards described in subsection (a) shall require at least 1 paper poll book (containing all of the information necessary to confirm that an individual is eligible to cast a vote at the site) for each such electronic poll book used at such voting site. (c) Deviation The standards described in subsection (a) shall permit States, upon giving reasonable public notice, to deviate from any allocation requirements in the case of unforeseen circumstances such as a natural disaster or terrorist attack. .\n**(2) Conforming amendment**\nSection 202 of such Act ( 52 U.S.C. 20922 ), as amended by section 3(c), is amended\u2014\n**(A)**\nby redesignating paragraphs (4), (5), and (6) as paragraphs (5), (6), and (7), respectively; and\n**(B)**\nby inserting after paragraph (4) the following new paragraph:\n(5) carrying out the duties described in subtitle E; .\n**(3) Clerical amendment**\nThe table of contents of such Act is amended by adding at the end of the items relating to title II the following:\nSubtitle E\u2014Guidance and Standards Sec. 299. Standards for establishing the minimum required voting systems and poll workers. .\n#### 5. Prohibition on campaign activities by chief State election administration officials\n##### (a) In General\nTitle III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ) is amended by inserting after section 319 the following new section:\n319A. Campaign activities by chief State election administration officials (a) Prohibition It shall be unlawful for a chief State election administration official to take an active part in political management or in a political campaign with respect to any election for Federal office over which such official has supervisory authority. (b) Chief State election administration official The term chief State election administration official means the highest State official with responsibility for the administration of Federal elections under State law. (c) Active part in political management or in a political campaign The term active part in political management or in a political campaign means\u2014 (1) serving as a member of an authorized committee of a candidate for Federal office; (2) the use of official authority or influence for the purpose of interfering with or affecting the result of an election for Federal office; (3) the solicitation, acceptance, or receipt of a contribution from any person on behalf of a candidate for Federal office; and (4) any other act which would be prohibited under paragraph (2) or (3) of section 7323(b) of title 5, United States Code, if taken by an individual to whom such paragraph applies (other than any prohibition on running for public office). (d) Exception in case of recusal from administration of elections involving election official or immediate family member (1) In general This section does not apply to a chief State election administration official with respect to an election for Federal office in which such official or an immediate family member of the official is a candidate, but only if\u2014 (A) such official recuses himself or herself from all of the official\u2019s responsibilities for the administration of such election; and (B) the official who assumes responsibility for supervising the administration of the election does not report directly to such official. (2) Immediate family member defined In paragraph (1), the term immediate family member means, with respect to a candidate, a father, mother, son, daughter, brother, sister, husband, wife, father-in-law, or mother-in-law. .\n##### (b) Effective Date\nThe amendments made by subsection (a) shall apply with respect to elections for Federal office held after January 1, 2027.\n#### 6. Payments to States to prevent unreasonable wait times and promote well-run elections\n##### (a) In general\nSubtitle D of title II of the Help America Vote Act of 2002 ( 52 U.S.C. 21001 et seq. ) is amended by adding at the end the following:\nVII Payments for preventing unreasonable voter wait times 297. Payments to States (a) In general The Commission shall make a payment to each eligible State. Such payments shall be made not later than 30 days after the date of enactment of this part. (b) Eligible State For purposes of this section, a State is an eligible State if such State has filed with the Commission a State plan covering the fiscal year in which the State describes how it intends to use the funds provided under this section. (c) Use of funds An eligible State shall use the payment received under this part to meet the requirements of sections 305 and 321. (d) Amount of payment (1) In general The amount of payment made to a State under this section shall be the minimum payment amount described in paragraph (2) plus the voting age population proportion amount described in paragraph (3). (2) Minimum payment amount The minimum payment amount described in this paragraph is\u2014 (A) in the case of any of the several States or the District of Columbia, one-half of 1 percent of the aggregate amount made available for payments under this section; and (B) in the case of the Commonwealth of Puerto Rico, Guam, American Samoa, or the United States Virgin Islands, one-tenth of 1 percent of such aggregate amount. (3) Voting age population proportion amount The voting age population proportion amount described in this paragraph is the product of\u2014 (A) the aggregate amount made available for payments under this section minus the total of all of the minimum payment amounts determined under paragraph (2); and (B) the voting age population proportion for the State (as defined in paragraph (4)). (4) Voting age population proportion defined The term voting age population proportion means, with respect to a State, the amount equal to the quotient of\u2014 (A) the voting age population of the State (as reported in the most recent decennial census); and (B) the total voting age population of all States (as reported in the most recent decennial census). (e) Authorization of appropriations (1) In general There are authorized to be appropriated for payments under this section $500,000,000 for each fiscal year. (2) Availability Any amounts appropriated pursuant to the authority of paragraph (1) shall remain available without fiscal year limitation until expended. .\n##### (b) Clerical amendment\nThe table of contents of such Act is amended by inserting after the item relating to section 296 the following:\nPart VII\u2014Payments for preventing unreasonable voter wait times Sec. 297. Payments to States. .",
      "versionDate": "2025-08-05",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-15T18:12:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-05",
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
          "measure-id": "id119hr4911",
          "measure-number": "4911",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4911v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>People Over Long Lines Act or the POLL Act</strong></p><p>This bill sets forth provisions related to voting and the administration of federal elections.</p><p>Specifically, the bill requires states to ensure that voters wait no more than 30 minutes at any polling place to cast their vote in a federal election, establishes a private right of action for voters who experience longer waiting times, and directs the Election Assistance Commission to make payments to eligible states to prevent unreasonable waiting times.</p><p>Next, the bill requires each state to provide for the minimum required number of voting systems, poll workers, and other election resources for each polling location on the day of any federal election and each day of early voting. The Department of Justice's Civil Rights Division must issue uniform standards regarding the minimum number and distribution of such systems, workers, and other resources.</p><p>The bill also prohibits a chief state election administration official from taking an active part in political management or in a political campaign with respect to any federal election over which the official has supervisory authority, with certain exceptions.</p>"
        },
        "title": "POLL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4911.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>People Over Long Lines Act or the POLL Act</strong></p><p>This bill sets forth provisions related to voting and the administration of federal elections.</p><p>Specifically, the bill requires states to ensure that voters wait no more than 30 minutes at any polling place to cast their vote in a federal election, establishes a private right of action for voters who experience longer waiting times, and directs the Election Assistance Commission to make payments to eligible states to prevent unreasonable waiting times.</p><p>Next, the bill requires each state to provide for the minimum required number of voting systems, poll workers, and other election resources for each polling location on the day of any federal election and each day of early voting. The Department of Justice's Civil Rights Division must issue uniform standards regarding the minimum number and distribution of such systems, workers, and other resources.</p><p>The bill also prohibits a chief state election administration official from taking an active part in political management or in a political campaign with respect to any federal election over which the official has supervisory authority, with certain exceptions.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4911"
    },
    "title": "POLL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>People Over Long Lines Act or the POLL Act</strong></p><p>This bill sets forth provisions related to voting and the administration of federal elections.</p><p>Specifically, the bill requires states to ensure that voters wait no more than 30 minutes at any polling place to cast their vote in a federal election, establishes a private right of action for voters who experience longer waiting times, and directs the Election Assistance Commission to make payments to eligible states to prevent unreasonable waiting times.</p><p>Next, the bill requires each state to provide for the minimum required number of voting systems, poll workers, and other election resources for each polling location on the day of any federal election and each day of early voting. The Department of Justice's Civil Rights Division must issue uniform standards regarding the minimum number and distribution of such systems, workers, and other resources.</p><p>The bill also prohibits a chief state election administration official from taking an active part in political management or in a political campaign with respect to any federal election over which the official has supervisory authority, with certain exceptions.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4911"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4911ih.xml"
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
      "title": "POLL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POLL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "People Over Long Lines Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to ensure that voters in elections for Federal office do not wait in long lines in order to vote, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:48Z"
    }
  ]
}
```
