# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/455
- Title: Protecting Sensitive Locations Act
- Congress: 119
- Bill type: S
- Bill number: 455
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-02-27T17:52:22Z
- Update date including text: 2026-02-27T17:52:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/455",
    "number": "455",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Protecting Sensitive Locations Act",
    "type": "S",
    "updateDate": "2026-02-27T17:52:22Z",
    "updateDateIncludingText": "2026-02-27T17:52:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
            "date": "2025-02-06T18:13:32Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T18:13:32Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
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
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-06",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "GA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "RI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NH"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "DE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "NY"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s455is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 455\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Blumenthal (for himself, Mr. Durbin , Mr. Booker , Ms. Cortez Masto , Mr. Schiff , Mrs. Murray , Mr. Padilla , Ms. Warren , Mr. Wyden , Mr. Heinrich , Mr. Hickenlooper , Ms. Rosen , Ms. Duckworth , Mr. Sanders , Ms. Hirono , Mr. Markey , Mr. Schatz , Mr. Welch , Mr. Warnock , Mr. Bennet , Mr. Whitehouse , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 287 of the Immigration and Nationality Act to limit immigration enforcement actions at sensitive locations, to clarify the powers of immigration officers at sensitive locations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Sensitive Locations Act .\n#### 2. Powers of immigration officers and employees at sensitive locations\n##### (a) In general\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) (1) In order to ensure individuals\u2019 access to sensitive locations, this subsection shall apply to any enforcement action by\u2014 (A) officers or agents of the Department of Homeland Security, including officers and agents of U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection; and (B) any individual designated to perform immigration enforcement functions pursuant to a written agreement described in subsection (g). (2) (A) An enforcement action may not take place, be focused on a location, or occur, within 1,000 feet of a sensitive location, except under exigent circumstances. (B) If an immigration enforcement action is taking place under exigent circumstances, and the exigent circumstances permitting the enforcement action cease, the enforcement action shall be discontinued until such exigent circumstances reemerge. (C) If an individual referred to in subparagraph (A) or (B) of paragraph (1) is not certain as to whether exigent circumstances exist, the individual\u2014 (i) shall cease the enforcement action immediately; (ii) shall consult with his or her supervisor in real time regarding the existence of exigent circumstances; and (iii) may not continue the enforcement action until the individual\u2019s supervisor affirmatively confirms the existence of exigent circumstances. (3) (A) When proceeding with an enforcement action at or near a sensitive location, individuals referred to in subparagraph (A) or (B) of paragraph (1) shall make every effort\u2014 (i) to conduct themselves as discreetly as possible, consistent with officer and public safety; (ii) to limit the time spent at the sensitive location; and (iii) to limit the enforcement action to the person or persons for whom prior approval was obtained. (B) If, in the course of an enforcement action that is not initiated at or focused on a sensitive location, individuals referred to in subparagraph (A) or (B) of paragraph (1) are led to or near a sensitive location, and no clear exigent circumstance with respect to the sensitive location exists, such individuals shall\u2014 (i) cease before taking any further enforcement action; (ii) conduct themselves in a discreet manner; (iii) maintain surveillance; and (iv) in the event that uncertainty exists about the existence of exigent circumstances, immediately consult their supervisor in order to determine whether such enforcement action should be discontinued pursuant to paragraph (2)(C). (C) This subsection shall not apply to the transportation of an individual apprehended at or near a land or sea border to a hospital or health care provider for the purpose of providing such individual medical care. (D) This subsection shall not apply to a rare premeditated arrest operation, undertaken with the prior written approval of an appropriate authorizing official, involving the targeted arrest of a terrorist suspect, an individual who poses a clear threat to national security, or an individual who poses an extraordinary danger to public safety. (4) If an enforcement action is carried out in violation of this subsection\u2014 (A) no information resulting from the enforcement action may be entered into the record or received into evidence in a removal proceeding resulting from the enforcement action; and (B) the alien who is the subject of such removal proceeding may file a motion for the immediate termination of the removal proceeding. (5) (A) Each official specified in subparagraph (B) shall ensure that the employees under the supervision of such official receive annual training in compliance with the requirements of this subsection, section 239, and section 384 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1367 ). (B) The officials specified in this subparagraph are the following: (i) The Chief Counsel of U.S. Immigration and Customs Enforcement. (ii) The Field Office Directors of U.S. Immigration and Customs Enforcement. (iii) Each Special Agent in Charge of U.S. Immigration and Customs Enforcement. (iv) Each Chief Patrol Agent of U.S. Customs and Border Protection. (v) The Director of Field Operations of U.S. Customs and Border Protection. (vi) The Director of Air and Marine Operations of U.S. Customs and Border Protection. (vii) The Internal Affairs Special Agent in Charge of U.S. Customs and Border Protection. (6) (A) Not later than 30 days after any enforcement action is taken at a sensitive location by any individual referred to in subparagraph (A) or (B) of paragraph (1), the Secretary of Homeland Security shall provide a report to both the Office of the Inspector General of the Department of Homeland Security and the Office for Civil Rights and Civil Liberties of the Department of Homeland Security for each such enforcement action, which shall contain\u2014 (i) the date, State, and local political subdivision (such as city, town, or county) in which each enforcement action occurred; (ii) the specific sensitive location site where the enforcement action occurred; (iii) the type of enforcement action that occurred; (iv) the specific department, agency, and officers responsible for the enforcement action; (v) a thorough description of the circumstances which purportedly justified the enforcement action, including either\u2014 (I) a clear description of the exigent circumstances involved; or (II) a certified copy of the written approval for the immigration arrest that was signed by an appropriate authorizing officer, along with a clear description of the specific and rare threat which justified the premeditated arrest at this sensitive location; (vi) a description of the intended target of the enforcement action; (vii) the number of individuals, if any, arrested or taken into custody through the enforcement action; (viii) the number of collateral arrests, if any, from the enforcement action and the reasons for each such arrest; and (ix) a certification of whether a supervisor was contacted prior to, during, or after each such enforcement action. (B) An appropriate committee of Congress may, at any time, request and successfully receive a confidential or redacted copy of any of the individual reports described in subparagraph (A). (7) (A) The Director of U.S. Immigration and Customs Enforcement and the Commissioner for U.S. Customs and Border Protection shall each submit an annual report to the appropriate committees of Congress that describes the enforcement actions undertaken by U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection, as applicable, during the preceding fiscal year that were covered by this subsection. (B) Each report submitted pursuant to subparagraph (A) shall include\u2014 (i) the number of enforcement actions at or focused on a sensitive location; (ii) the number of enforcement actions where officers or agents were subsequently led to or near a sensitive location; (iii) the date, site, State, and local political subdivision (such as city, town, or county) in which each enforcement action covered by clause (i) or (ii) occurred; (iv) the component of the agency responsible for each such enforcement action; (v) a description of the intended target of each such enforcement action; (vi) the number of individuals, if any, arrested or taken into custody through each such enforcement action; (vii) the number of collateral arrests, if any, from each such enforcement action and the reasons for each such arrest; and (viii) a certification of whether the location administrator was contacted prior to, during, or after each such enforcement action. (8) (A) The Office of the Inspector General of the Department of Homeland Security shall submit an annual report to the appropriate committees of Congress regarding the complaints of enforcement actions taken in sensitive locations by U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection during the preceding year that were covered by this subsection. (B) Each report submitted pursuant to subparagraph (A) shall include\u2014 (i) the number of complaints of enforcement actions reported at, or focused on, a sensitive location; (ii) the reported date, site, State, and local political subdivision (such as city, town, or county) in which each enforcement action referred to in clause (i) occurred; (iii) the reported agency responsible for each such enforcement action; (iv) a description of the intended target of each such enforcement action; (v) the reported number of individuals, if any, arrested or taken into custody through each such enforcement action; (vi) the reported number of collateral arrests, if any, from each such enforcement action, and the reasons for each such arrest; and (vii) if available, a certification of whether the location administrator was contacted prior to, during, or after each such enforcement action. (9) In this subsection: (A) The term appropriate authorizing official means\u2014 (i) in the case of officers and agents of U.S. Immigration and Customs Enforcement\u2014 (I) the Assistant Director of Operations, Homeland Security Investigations; (II) the Executive Associate Director of Homeland Security Investigations; (III) the Assistant Director for Field Operations, Enforcement, and Removal Operations; (IV) the Executive Associate Director for Field Operations, Enforcement, and Removal Operations; or (V) any other individual who is determined to be an appropriate authorizing official by the Secretary of Homeland Security; and (ii) in the case of officers and agents of U.S. Customs and Border Protection\u2014 (I) a Chief Patrol Agent; (II) the Director of Field Operations; (III) the Director of Air and Marine Operations; (IV) the Internal Affairs Special Agent in Charge; or (V) any other individual who is determined to be an appropriate authorizing official by the Secretary of Homeland Security; and (iii) in the case of all other individuals referred to in subparagraph (A) or (B) of paragraph (1), an official determined under rules promulgated by the Secretary of Homeland Security not later than 90 days after the date of the enactment of the Protecting Sensitive Locations Act . (B) The term appropriate committees of Congress means\u2014 (i) the Committee on Homeland Security and Governmental Affairs of the Senate ; (ii) the Committee on the Judiciary of the Senate ; (iii) the Committee on Appropriations of the Senate ; (iv) the Committee on Homeland Security of the House of Representatives ; (v) the Committee on the Judiciary of the House of Representatives ; and (vi) the Committee on Appropriations of the House of Representatives . (C) The term early childhood education program has the meaning given such term in section 103(8) of the Higher Education Act of 1965 ( 20 U.S.C. 1003(8) ). (D) The term enforcement action \u2014 (i) means an apprehension, arrest, interview, request for identification, search, or surveillance for the purposes of immigration enforcement; and (ii) includes an enforcement action at, or focused on, a sensitive location that is part of a joint case led by another law enforcement agency. (E) The term exigent circumstances means a situation involving\u2014 (i) the imminent risk of death, violence, or physical harm to any person, including a situation implicating terrorism or the national security of the United States in some other manner; (ii) the immediate arrest or hot pursuit of an individual presenting an imminent danger to public safety, including the imminent risk of death, violence, or physical harm to a person; (iii) a rare, premeditated arrest operation described in paragraph (3)(D), undertaken with the prior written approval of an appropriate authorizing official, involving the targeted arrest of a terrorist suspect, an individual who poses a clear threat to national security, or an individual who poses an extraordinary danger to public safety; (iv) a direct threat to national security; or (v) the imminent risk of destruction of evidence that is material to an ongoing criminal case. (F) The term sensitive location includes all of the physical space located within 1,000 feet of\u2014 (i) any medical or mental healthcare facility, including any hospital, health care practitioner\u2019s office, accredited health clinic, vaccination or testing site, or emergent or urgent care facility, or community health center; (ii) any public or private school (including preschools, primary schools, secondary schools, and postsecondary schools (including colleges and universities)), any site of an early childhood education program, any other institution of learning, such as vocational or trade schools, and any other site where individuals who are unemployed or underemployed may apply for or receive workforce training; (iii) any scholastic or education-related activity or event, including field trips and interscholastic events; (iv) any school bus or school bus stop during periods when school children are present on the bus or at the stop; (v) any recreational facility for children, such as playgrounds and formal recreational facilities; (vi) any child care focused facility, including child care centers, before or after school care centers, foster care facilities, and group homes for children; (vii) any location where disaster or emergency response and relief is being provided by Federal, State, or local entities, such as the distribution of emergency supplies, food, and water; any place of temporary shelter; any place along an evacuation route; and any site where registration for disaster-related assistance or family reunification is taking place; (viii) any location of any organization that\u2014 (I) assists children, pregnant women, victims of crime or abuse, or individuals with significant mental or physical disabilities, including domestic violence shelters, child advocacy centers, facilities that serve disabled persons, drug or alcohol counseling and treatment facilities, rape crisis centers, supervised visitation centers, family justice centers, victims\u2019 services providers, and community-based organizations providing social services; or (II) provides disaster or emergency social services and assistance, or services for individuals experiencing homelessness, including food banks, pantries, or other establishments distributing food, and shelters; (ix) any church, synagogue, mosque, or other place of worship or religious study, such as buildings rented for the purpose of religious services, or a temporary facility or location where such activities are taking place; (x) any sites of a funeral, graveside ceremony, wedding, or any site where other religious or civil ceremonies or observances are occurring; (xi) any site during the occurrence of a public demonstration, such as a march, rally, or parade; (xii) any Federal, State, or local courthouse, including the office of an individual\u2019s legal counsel or representative, and a probation office; (xiii) any congressional district office; (xiv) any Social Security office; (xv) any public assistance offices, including locations where individuals may apply for or receive unemployment compensation or report violations of labor and employment laws; (xvi) the indoor or outdoor premises of a department of motor vehicles; (xvii) a polling place, including any building or infrastructure where voting takes place during an election; (xviii) a labor union hall or any other union-operated building or office where registered applicants are referred in rotation to jobs; (xix) any public library; or (xx) any other locations specified by the Secretary of Homeland Security for purposes of this subsection. (G) The term supervisor means an official determined under rules promulgated by the Secretary of Homeland Security pursuant to section 2(c) of the Protecting Sensitive Locations Act . .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 90 days after the date of the enactment of this Act.\n##### (c) Rulemaking\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Homeland Security shall promulgate regulations to carry out the amendment made by subsection (a).",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1061",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Sensitive Locations Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-13T13:57:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s455",
          "measure-number": "455",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s455v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Sensitive Locations Act</strong></p><p>This bill prohibits immigration enforcement actions within 1,000 feet of a sensitive location except in exigent circumstances, such as the\u00a0imminent risk of death, violence, or physical harm to any person.</p><p>Sensitive locations include\u00a0</p><ul><li>health care facilities;</li><li>schools and school bus stops;</li><li>places that provide assistance for people such as children, pregnant women, and abuse victims;</li><li>child care facilities;</li><li>places that provide disaster or emergency services;</li><li>places of worship;</li><li>courthouses and lawyers\u2019 offices;</li><li>facilities\u00a0used as polling\u00a0places;</li><li>certain labor union facilities; and</li><li>public assistance offices.</li></ul><p>The prohibition shall apply to Department of Homeland Security officers and agents, as well as state employees pursuing immigration enforcement actions.</p><p>If an enforcement action is carried out in violation of this prohibition (1) no information resulting from the action may be entered into the record in a resulting removal proceeding, and (2) the affected individual may move to immediately terminate such a proceeding.</p><p>U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection shall annually report to Congress about enforcement actions taken at sensitive locations in the preceding year.\u00a0</p>"
        },
        "title": "Protecting Sensitive Locations Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s455.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Sensitive Locations Act</strong></p><p>This bill prohibits immigration enforcement actions within 1,000 feet of a sensitive location except in exigent circumstances, such as the\u00a0imminent risk of death, violence, or physical harm to any person.</p><p>Sensitive locations include\u00a0</p><ul><li>health care facilities;</li><li>schools and school bus stops;</li><li>places that provide assistance for people such as children, pregnant women, and abuse victims;</li><li>child care facilities;</li><li>places that provide disaster or emergency services;</li><li>places of worship;</li><li>courthouses and lawyers\u2019 offices;</li><li>facilities\u00a0used as polling\u00a0places;</li><li>certain labor union facilities; and</li><li>public assistance offices.</li></ul><p>The prohibition shall apply to Department of Homeland Security officers and agents, as well as state employees pursuing immigration enforcement actions.</p><p>If an enforcement action is carried out in violation of this prohibition (1) no information resulting from the action may be entered into the record in a resulting removal proceeding, and (2) the affected individual may move to immediately terminate such a proceeding.</p><p>U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection shall annually report to Congress about enforcement actions taken at sensitive locations in the preceding year.\u00a0</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s455"
    },
    "title": "Protecting Sensitive Locations Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Sensitive Locations Act</strong></p><p>This bill prohibits immigration enforcement actions within 1,000 feet of a sensitive location except in exigent circumstances, such as the\u00a0imminent risk of death, violence, or physical harm to any person.</p><p>Sensitive locations include\u00a0</p><ul><li>health care facilities;</li><li>schools and school bus stops;</li><li>places that provide assistance for people such as children, pregnant women, and abuse victims;</li><li>child care facilities;</li><li>places that provide disaster or emergency services;</li><li>places of worship;</li><li>courthouses and lawyers\u2019 offices;</li><li>facilities\u00a0used as polling\u00a0places;</li><li>certain labor union facilities; and</li><li>public assistance offices.</li></ul><p>The prohibition shall apply to Department of Homeland Security officers and agents, as well as state employees pursuing immigration enforcement actions.</p><p>If an enforcement action is carried out in violation of this prohibition (1) no information resulting from the action may be entered into the record in a resulting removal proceeding, and (2) the affected individual may move to immediately terminate such a proceeding.</p><p>U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection shall annually report to Congress about enforcement actions taken at sensitive locations in the preceding year.\u00a0</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s455"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s455is.xml"
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
      "title": "Protecting Sensitive Locations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Sensitive Locations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 287 of the Immigration and Nationality Act to limit immigration enforcement actions at sensitive locations, to clarify the powers of immigration officers at sensitive locations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:28Z"
    }
  ]
}
```
