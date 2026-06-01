# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/558
- Title: Antisemitism Awareness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 558
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-09T12:03:18Z
- Update date including text: 2025-12-09T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S973-974)
- 2025-04-30 - Committee: Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S973-974)
- 2025-04-30 - Committee: Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/558",
    "number": "558",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Antisemitism Awareness Act of 2025",
    "type": "S",
    "updateDate": "2025-12-09T12:03:18Z",
    "updateDateIncludingText": "2025-12-09T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Committee consideration and Mark Up Session held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S973-974)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
            "date": "2025-04-30T21:39:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-13T16:12:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OK"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SC"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NH"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ME"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WY"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CO"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ID"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AR"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CO"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AR"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ND"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MS"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "VA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "WY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "AZ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "CA"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "SD"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "LA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "WV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "AK"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SD"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-08",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s558is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 558\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Scott of South Carolina (for himself, Ms. Rosen , Mr. Lankford , Mr. Schumer , Mr. Graham , Mr. Blumenthal , Mr. Scott of Florida , Ms. Hassan , Ms. Collins , Mrs. Gillibrand , Mrs. Capito , Mr. Gallego , Mr. Barrasso , Mr. Hickenlooper , Mr. Crapo , Mr. Wyden , Mrs. Britt , Mr. Coons , Mr. Cornyn , Ms. Cortez Masto , Mr. Cotton , Mr. Bennet , Mr. Boozman , Ms. Cantwell , Mr. Ricketts , Mr. Fetterman , Mr. Grassley , Mr. Schiff , Mr. Cramer , Ms. Slotkin , Mrs. Hyde-Smith , Mr. Warner , Mrs. Fischer , Mr. Peters , Mr. Daines , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for the consideration of a definition of antisemitism set forth by the International Holocaust Remembrance Alliance for the enforcement of Federal antidiscrimination laws concerning education programs or activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Antisemitism Awareness Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ntitle VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), prohibits discrimination on the basis of race, color, and national origin in programs and activities receiving Federal financial assistance;\n**(2)**\nwhile such title does not cover discrimination based solely on religion, individuals who face discrimination based on actual or perceived shared ancestry or ethnic characteristics do not lose protection under such title for also being members of a group that share a common religion;\n**(3)**\ndiscrimination against Jews may give rise to a violation of such title when the discrimination is based on race, color, or national origin, which can include discrimination based on actual or perceived shared ancestry or ethnic characteristics;\n**(4)**\nit is the policy of the United States to enforce such title against prohibited forms of discrimination rooted in antisemitism as vigorously as against all other forms of discrimination prohibited by such title; and\n**(5)**\nas noted in the U.S. National Strategy to Counter Antisemitism issued by the White House on May 25, 2023, it is critical to\u2014\n**(A)**\nincrease awareness and understanding of antisemitism, including its threat to America;\n**(B)**\nimprove safety and security for Jewish communities;\n**(C)**\nreverse the normalization of antisemitism and counter antisemitic discrimination; and\n**(D)**\nexpand communication and collaboration between communities.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nAntisemitism is on the rise in the United States and is impacting Jewish students in K\u201312 schools, colleges, and universities.\n**(2)**\nThe International Holocaust Remembrance Alliance (referred to in this Act as the IHRA ) Working Definition of Antisemitism is a vital tool which helps individuals understand and identify the various manifestations of antisemitism.\n**(3)**\nOn December 11, 2019, Executive Order 13899 extended protections against discrimination under the Civil Rights Act of 1964 to individuals subjected to antisemitism on college and university campuses and tasked Federal agencies to consider the IHRA Working Definition of Antisemitism when enforcing title VI of such Act.\n**(4)**\nSince 2018, the Department of Education has used the IHRA Working Definition of Antisemitism when investigating violations of that title VI.\n**(5)**\nThe use of alternative definitions of antisemitism impairs enforcement efforts by adding multiple standards and may fail to identify many of the modern manifestations of antisemitism.\n**(6)**\nThe White House released the first-ever United States National Strategy to Counter Antisemitism on May 25, 2023, making clear that the fight against this hate is a national, bipartisan priority that must be successfully conducted through a whole-of-government-and-society approach.\n#### 4. Definitions\nFor purposes of this Act, the term definition of antisemitism \u2014\n**(1)**\nmeans the definition of antisemitism adopted on May 26, 2016, by the IHRA, of which the United States is a member, which definition has been adopted by the Department of State; and\n**(2)**\nincludes the [c]ontemporary examples of antisemitism identified in the IHRA definition.\n#### 5. Rule of construction for title VI of the Civil Rights Act of 1964\nIn reviewing, investigating, or deciding whether there has been a violation of title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ) on the basis of race, color, or national origin, based on an individual\u2019s actual or perceived shared Jewish ancestry or Jewish ethnic characteristics, the Department of Education shall take into consideration the definition of antisemitism as part of the Department\u2019s assessment of whether the practice was motivated by antisemitic intent.\n#### 6. Other rules of construction\n##### (a) General rule of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto expand the authority of the Secretary of Education;\n**(2)**\nto alter the standards pursuant to which the Department of Education makes a determination that harassing conduct amounts to actionable discrimination; or\n**(3)**\nto diminish or infringe upon the rights protected under any other provision of law that is in effect as of the date of enactment of this Act.\n##### (b) Constitutional protections\nNothing in this Act shall be construed to diminish or infringe upon any right protected under the First Amendment to the Constitution of the United States.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1007",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Antisemitism Awareness Act of 2025",
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
            "name": "First Amendment rights",
            "updateDate": "2025-04-11T18:26:55Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-11T18:26:55Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-04-11T18:26:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-12T17:15:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s558",
          "measure-number": "558",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-09-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s558v00",
            "update-date": "2025-09-05"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Antisemitism Awareness Act of 2025</strong></p><p>This bill provides statutory authority for the requirement that the Department of Education\u2019s Office for Civil Rights take into consideration the International Holocaust Remembrance Alliance's (IHRA's) working definition of antisemitism when reviewing or investigating complaints of discrimination based on race, color, or national origin in programs or activities that receive federal financial assistance.\u00a0According to the IHRA's working definition, <em>antisemitism</em> is a certain perception of Jews, which may be expressed as hatred toward Jews.\u00a0</p>"
        },
        "title": "Antisemitism Awareness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s558.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Antisemitism Awareness Act of 2025</strong></p><p>This bill provides statutory authority for the requirement that the Department of Education\u2019s Office for Civil Rights take into consideration the International Holocaust Remembrance Alliance's (IHRA's) working definition of antisemitism when reviewing or investigating complaints of discrimination based on race, color, or national origin in programs or activities that receive federal financial assistance.\u00a0According to the IHRA's working definition, <em>antisemitism</em> is a certain perception of Jews, which may be expressed as hatred toward Jews.\u00a0</p>",
      "updateDate": "2025-09-05",
      "versionCode": "id119s558"
    },
    "title": "Antisemitism Awareness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Antisemitism Awareness Act of 2025</strong></p><p>This bill provides statutory authority for the requirement that the Department of Education\u2019s Office for Civil Rights take into consideration the International Holocaust Remembrance Alliance's (IHRA's) working definition of antisemitism when reviewing or investigating complaints of discrimination based on race, color, or national origin in programs or activities that receive federal financial assistance.\u00a0According to the IHRA's working definition, <em>antisemitism</em> is a certain perception of Jews, which may be expressed as hatred toward Jews.\u00a0</p>",
      "updateDate": "2025-09-05",
      "versionCode": "id119s558"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s558is.xml"
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
      "title": "Antisemitism Awareness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Antisemitism Awareness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the consideration of a definition of antisemitism set forth by the International Holocaust Remembrance Alliance for the enforcement of Federal antidiscrimination laws concerning education programs or activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:10Z"
    }
  ]
}
```
