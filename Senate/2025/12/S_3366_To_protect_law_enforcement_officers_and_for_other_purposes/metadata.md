# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3366?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3366
- Title: Back the Blue Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3366
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-03-05T22:19:35Z
- Update date including text: 2026-03-05T22:19:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3366",
    "number": "3366",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Back the Blue Act of 2025",
    "type": "S",
    "updateDate": "2026-03-05T22:19:35Z",
    "updateDateIncludingText": "2026-03-05T22:19:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
            "date": "2025-12-04T19:58:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-04T19:58:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IN"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AR"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "ND"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "ID"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NE"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "SC"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WV"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "KS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "OK"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NE"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "SD"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "AL"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "LA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "OK"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "SC"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NC"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "AK"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3366is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3366\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Cornyn (for himself, Mr. Banks , Mr. Barrasso , Mrs. Blackburn , Mr. Boozman , Mrs. Britt , Mr. Budd , Mrs. Capito , Mr. Cramer , Mr. Crapo , Mr. Cruz , Mr. Daines , Ms. Ernst , Mrs. Fischer , Mr. Graham , Mr. Grassley , Mr. Hagerty , Mrs. Hyde-Smith , Mr. Justice , Mr. Kennedy , Mr. Lee , Ms. Lummis , Mr. Marshall , Mr. McCormick , Mr. Mullin , Mr. Ricketts , Mr. Risch , Mr. Rounds , Mr. Scott of Florida , Mr. Sheehy , Mr. Tuberville , Mr. Young , Mr. Cassidy , Mr. Lankford , Mr. Scott of South Carolina , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Back the Blue Act of 2025 .\n#### 2. Protection of law enforcement officers\n##### (a) Killing of law enforcement officers\n**(1) Offense**\nChapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. Killing of law enforcement officers (a) Definitions In this section\u2014 (1) the terms Federal law enforcement officer and United States judge have the meanings given those terms in section 115; (2) the term federally funded public safety officer means a public safety officer or judicial officer for a public agency that\u2014 (A) receives Federal financial assistance; and (B) is an agency of an entity that is a State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, any other territory or possession of the United States, or an Indian tribe, or a unit of local government of such entity; (3) the term firefighter includes an individual serving as an official recognized or designated member of a legally organized volunteer fire department and an officially recognized or designated public employee member of a rescue squad or ambulance crew; (4) the term judicial officer means a judge or other officer or employee of a court, including prosecutors, court security, pretrial services officers, court reporters, and corrections, probation, and parole officers; (5) the term law enforcement officer means an individual authorized by law to engage in or supervise the enforcement, prevention, detection, investigation, arrest, apprehension, prosecution, or incarceration of any person for any violation of criminal law; (6) the term public agency includes a court system, the National Guard of a State to the extent the personnel of that National Guard are not in Federal service, and the defense forces of a State authorized by section 109 of title 32; and (7) the term public safety officer means an individual serving a public agency in an official capacity, as a law enforcement officer, as a firefighter, as a chaplain, or as a member of a rescue squad or ambulance crew. (b) Offense It shall be unlawful for any person to\u2014 (1) kill, or attempt or conspire to kill\u2014 (A) a United States judge; (B) a Federal law enforcement officer; or (C) a federally funded public safety officer while that officer is engaged in official duties, or on account of the performance of official duties; or (2) kill a former United States judge, Federal law enforcement officer, or federally funded public safety officer on account of the past performance of official duties. (c) Penalty Any person that violates subsection (b) shall be fined under this title and imprisoned for not less than 10 years or for life, or, if death results, shall be sentenced to not less than 30 years and not more than life, or may be punished by death. .\n**(2) Table of sections**\nThe table of sections for chapter 51 of title 18, United States Code, is amended by adding at the end the following:\n1123. Killing of law enforcement officers. .\n##### (b) Assault of law enforcement officers\n**(1) Offense**\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assaults of law enforcement officers (a) Definition In this section, the term federally funded State or local law enforcement officer means an individual involved in the enforcement, prevention, detection, investigation, arrest, apprehension, prosecution, or incarceration of any person for any violation of criminal law (including a police, corrections, probation, or parole officer) who works for a public agency (that receives Federal financial assistance) of a State of the United States or the District of Columbia. (b) Offense It shall be unlawful to assault a federally funded State or local law enforcement officer while engaged in or on account of the performance of official duties, or assault any person who formerly served as a federally funded State or local law enforcement officer on account of the performance of such person's official duties during such service, or because of the actual or perceived status of the person as a federally funded State or local law enforcement officer. (c) Penalty Any person who violates subsection (b) shall be subject to a fine under this title and\u2014 (1) if the assault resulted in bodily injury (as defined in section 1365), shall be imprisoned not less than 2 years and not more than 10 years; (2) if the assault resulted in substantial bodily injury (as defined in section 113), shall be imprisoned not less than 5 years and not more than 20 years; (3) if the assault resulted in serious bodily injury (as defined in section 1365), shall be imprisoned for not less than 10 years; (4) if a deadly or dangerous weapon was used during and in relation to the assault, shall be imprisoned for not less than 20 years; and (5) shall be imprisoned for not more than 1 year in any other case. (d) Certification requirement (1) In general No prosecution of any offense described in this section may be undertaken by the United States, except under the certification in writing of the Attorney General, or a designee, that\u2014 (A) the State does not have jurisdiction; (B) the State has requested that the Federal Government assume jurisdiction; or (C) a prosecution by the United States is in the public interest and necessary to secure substantial justice, as determined by the Attorney General, based on\u2014 (i) the verdict or sentence obtained pursuant to State charges; (ii) the extent of planning and premeditation involved in the offense; (iii) the intended outcome of the conduct; (iv) the disregard for human life, including collateral damage to unintended victims, involved in the offense; and (v) the benefit to public safety from Federal prosecution. (2) Rule of construction Nothing in this subsection shall be construed to limit the authority of Federal officers, or a Federal grand jury, to investigate possible violations of this section. (e) Statute of limitations (1) Offenses not resulting in death Except as provided in paragraph (2), no person shall be prosecuted, tried, or punished for any offense under this section unless the indictment for such offense is found, or the information for such offense is instituted, not later than 7 years after the date on which the offense was committed. (2) Offenses resulting in death An indictment or information alleging that an offense under this section resulted in death may be found or instituted at any time without limitation. .\n**(2) Table of sections**\nThe table of sections for chapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assaults of law enforcement officers. .\n##### (c) Flight To avoid prosecution for killing law enforcement officials\n**(1) Offense**\nChapter 49 of title 18, United States Code, is amended by adding at the end the following:\n1075. Flight to avoid prosecution for killing law enforcement officials (a) Offense It shall be unlawful for any person to move or travel in interstate or foreign commerce with intent to avoid prosecution, or custody or confinement after conviction, under the laws of the place from which the person flees or under section 1114 or 1123, for a crime consisting of the killing, an attempted killing, or a conspiracy to kill a Federal judge or Federal law enforcement officer (as those terms are defined in section 115), or a federally funded public safety officer (as that term is defined in section 1123). (b) Penalty Any person that violates subsection (a) shall be fined under this title and imprisoned for not less than 10 years, in addition to any other term of imprisonment for any other offense relating to the conduct described in subsection (a). .\n**(2) Table of sections**\nThe table of sections for chapter 49 of title 18, United States Code, is amended by adding at the end the following:\n1075. Flight to avoid prosecution for killing law enforcement officials. .\n#### 3. Specific aggravating factor for Federal death penalty killing of law enforcement officer\n##### (a) Aggravating factors for homicide\nSection 3592(c) of title 18, United States Code, is amended by inserting after paragraph (16) the following:\n(17) Killing of a law enforcement officer, prosecutor, judge, or first responder The defendant killed or attempted to kill a person who is authorized by law\u2014 (A) to engage in or supervise the prevention, detention, or investigation of any criminal violation of law; (B) to arrest, prosecute, or adjudicate an individual for any criminal violation of law; or (C) to be a firefighter or other first responder. .\n#### 4. Limitation on Federal habeas relief for murders of law enforcement officers\n##### (a) Justice for law enforcement officers and their families\n**(1) In general**\nSection 2254 of title 28, United States Code, is amended by adding at the end the following:\n(j) (1) For an application for a writ of habeas corpus on behalf of a person in custody pursuant to the judgment of a State court for a crime that involved the killing of a public safety officer (as that term is defined in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 )) or judge, while the public safety officer or judge was engaged in the performance of official duties, or on account of the performance of official duties by or status as a public safety officer or judge\u2014 (A) the application shall be subject to the time limitations and other requirements under sections 2263, 2264, and 2266; and (B) the court shall not consider claims relating to sentencing that were adjudicated in a State court. (2) Sections 2251, 2262, and 2101 are the exclusive sources of authority for Federal courts to stay a sentence of death entered by a State court in a case described in paragraph (1). .\n**(2) Rules**\nRule 11 of the Rules Governing Section 2254 Cases in the United States District Courts is amended by adding at the end the following: Rule 60(b)(6) of the Federal Rules of Civil Procedure shall not apply to a proceeding under these rules in a case that is described in section 2254(j) of title 28, United States Code. .\n**(3) Finality of determination**\nSection 2244(b)(3)(E) of title 28, United States Code, is amended by striking the subject of a petition and all that follows and inserting: reheard in the court of appeals or reviewed by writ of certiorari. .\n**(4) Effective date and applicability**\n**(A) In general**\nThis paragraph and the amendments made by this paragraph shall apply to any case pending on or after the date of enactment of this Act.\n**(B) Time limits**\nIn a case pending on the date of enactment of this Act, if the amendments made by this paragraph impose a time limit for taking certain action, the period of which began before the date of enactment of this Act, the period of such time limit shall begin on the date of enactment of this Act.\n**(C) Exception**\nThe amendments made by this paragraph shall not bar consideration under section 2266(b)(3)(B) of title 28, United States Code, of an amendment to an application for a writ of habeas corpus that is pending on the date of enactment of this Act, if the amendment to the petition was adjudicated by the court prior to the date of enactment of this Act.\n#### 5. Limitation on recovery of certain damages for individuals engaged in felonies or crimes of violence\n##### (a) In general\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended by striking except that in any action and all that follows through For purposes and inserting the following: \u201cexcept that\u2014\n(1) in any action brought against a judicial officer for an act or omission taken in the judicial capacity of that officer, injunctive relief shall not be granted unless a declaratory decree was violated or declaratory relief was unavailable; and (2) in any action seeking redress for any deprivation that was incurred in the course of, or as a result of, or is related to, conduct by the injured party that, more likely than not, constituted a felony or a crime of violence (as that term is defined in section 16 of title 18, United States Code) (including any deprivation in the course of arrest or apprehension for, or the investigation, prosecution, or adjudication of, such an offense), a court may not award damages other than for necessary out-of-pocket expenditures and other monetary loss. For purposes .\n##### (b) Attorney\u2019s fees\nSection 722(b) of the Revised Statutes ( 42 U.S.C. 1988(b) ) is amended by striking except that in any action and all that follows and inserting the following: \u201cexcept that\u2014\n(1) in any action brought against a judicial officer for an act or omission taken in the judicial capacity of that officer, such officer shall not be held liable for any costs, including attorneys fees, unless such action was clearly in excess of the jurisdiction of that officer; and (2) in any action seeking redress for any deprivation that was incurred in the course of, or as a result of, or is related to, conduct by the injured party that, more likely than not, constituted a felony or a crime of violence (as that term is defined in section 16 of title 18, United States Code) (including any deprivation in the course of arrest or apprehension for, or the investigation, prosecution, or adjudication of, such an offense), the court may not allow such party to recover attorney\u2019s fees. .\n#### 6. Self-defense rights for law enforcement officers\n##### (a) In general\nChapter 203 of title 18, United States Code, is amended by inserting after section 3053 the following:\n3054. Authority of law enforcement officers to carry firearms Any sworn officer, agent, or employee of the United States, a State, or a political subdivision thereof, who is authorized by law to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of law, or to supervise or secure the safety of incarcerated inmates, may carry firearms if authorized by law to do so. Such authority to carry firearms, with respect to the lawful performance of the official duties of a sworn officer, agent, or employee of a State or a political subdivision thereof, shall include possession incident to depositing a firearm within a secure firearms storage area for use by all persons who are authorized to carry a firearm within any building or structure classified as a Federal facility or Federal court facility, as those terms are defined under section 930, and any grounds appurtenant to such a facility. .\n##### (b) Carrying of concealed firearms by qualified law enforcement officers\nSection 926B(e)(2) of title 18, United States Code, is amended by inserting any magazine and after includes .\n##### (c) Carrying of concealed firearms by qualified retired law enforcement officers\nSection 926C(e)(1)(B) of title 18, United States Code, is amended by inserting any magazine and after includes .\n##### (d) School zones\nSection 922(q)(2)(B)(vi) title 18, United States Code, is amended by inserting , a qualified law enforcement officer (as defined in section 926B), or a qualified retired law enforcement officer (as defined in section 926C) before the semicolon.\n##### (e) Regulations required\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall promulgate regulations allowing persons described in section 3054 of title 18, United States Code, to possess firearms in a manner described by that section. With respect to Federal justices, judges, bankruptcy judges, and magistrate judges, such regulations shall be prescribed after consultation with the Judicial Conference of the United States.\n##### (f) Table of sections\nThe table of sections for chapter 203 of title 18, United States Code, is amended by inserting after the item relating to section 3053 the following:\n3054. Authority of law enforcement officers to carry firearms. .\n##### (g) Further amendments\nSection 930 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(4) the possession of a firearm or ammunition in a Facility Security Level I or II civilian public access facility by a qualified law enforcement officer (as defined in section 926B(c)) or a qualified retired law enforcement officer (as defined in section 926C(c)). ; and\n**(2)**\nin subsection (g), by adding at the end the following:\n(4) The term Facility Security Level means a security risk assessment level assigned to a Federal facility by the security agency of the facility in accordance with the biannually issued Interagency Security Committee Standard. (5) The term civilian public access facility means a facility open to the general public. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4310",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Back the Blue Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-07T16:40:16Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3366is.xml"
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
      "title": "Back the Blue Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Back the Blue Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:18Z"
    }
  ]
}
```
