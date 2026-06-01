# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/726?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/726
- Title: A bill to amend chapter 44 of title 18, United States Code, to require the safe storage of firearms, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 726
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-02-06T11:56:28Z
- Update date including text: 2026-02-06T11:56:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/726",
    "number": "726",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "A bill to amend chapter 44 of title 18, United States Code, to require the safe storage of firearms, and for other purposes.",
    "type": "S",
    "updateDate": "2026-02-06T11:56:28Z",
    "updateDateIncludingText": "2026-02-06T11:56:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
            "date": "2025-02-25T22:13:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-25T22:13:14Z",
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
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-25",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NM"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NH"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "DE"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NV"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "AZ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "AZ"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "HI"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "DE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MD"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s726is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 726\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Blumenthal (for himself, Mr. Murphy , Mr. Schiff , Mr. Sanders , Mr. Padilla , Ms. Cantwell , Mr. Luj\u00e1n , Mr. Schumer , Mrs. Shaheen , Mrs. Gillibrand , Mr. Durbin , Mr. Warnock , Mr. Van Hollen , Mr. Coons , Ms. Rosen , Mrs. Murray , Mr. Merkley , Mr. Hickenlooper , Mr. Markey , Mr. Booker , Ms. Hirono , Mr. Reed , Mr. Wyden , Mr. Kelly , Ms. Warren , Mr. King , Mr. Fetterman , Ms. Duckworth , Mr. Bennet , Mr. Kaine , Mr. Welch , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend chapter 44 of title 18, United States Code, to require the safe storage of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Ethan's Law .\n#### 2. Findings\nCongress find the following:\n**(1)**\nAn estimated 4,600,000 minors in the United States live in homes with at least 1 unsecured firearm.\n**(2)**\nSeventy-three percent of children under the age of 10 living in homes with firearms reported knowing the location of their parents\u2019 firearms. Thirty-six percent of those children reported handling their parents\u2019 unsecured firearms.\n**(3)**\nThe presence of unsecured firearms in the home increases the risk of unintentional and intentional shootings. Over 75 percent of firearms used in youth suicide attempts and unintentional firearm injuries were stored in the residence of the victim, a relative, or a friend.\n**(4)**\nThe United States Secret Service and the Department of Education report that in 65 percent of deadly school shootings, the attacker obtained the firearm from his or her own home or that of a relative.\n**(5)**\nIn the last decade, nearly 2,000,000 firearms have been reported stolen. In 2016 alone, 238,000 firearms were reported stolen in the United States. Between 2010 and 2016, police recovered more than 23,000 stolen firearms across jurisdictions that were used to commit kidnappings, armed robberies, sexual assaults, murders, and other violent crimes.\n**(6)**\nHigher levels of neighborhood gun violence drive depopulation, discourage commercial activity, and decrease property values, resulting in fewer business establishments, fewer jobs, lower home values, and lower home ownership rates.\n**(7)**\nThe negative economic impact of gun violence in communities is tied directly to the national economy and interstate commerce.\n**(8)**\nCongress has the power under the interstate commerce clause and other provisions of the Constitution of the United States to enact measures ensuring firearms are securely stored.\n#### 3. Secure gun storage or safety device\nSection 922(z) of title 18, United States Code, is amended by adding at the end the following:\n(4) Secure gun storage by owners (A) Offense (i) In general Except as provided in clause (ii), it shall be unlawful for a person to store or keep any firearm that has moved in, or that has otherwise affected, interstate or foreign commerce on the premises of a residence under the control of the person if the person knows, or reasonably should know, that\u2014 (I) a minor is likely to gain access to the firearm without the permission of the parent or guardian of the minor; or (II) a resident of the residence is ineligible to possess a firearm under Federal, State, or local law. (ii) Exception Clause (i) shall not apply to a person if the person\u2014 (I) keeps the firearm\u2014 (aa) secure using a secure gun storage or safety device; or (bb) in a location that a reasonable person would believe to be secure; or (II) carries the firearm on his or her person or within such close proximity thereto that the person can readily retrieve and use the firearm as if the person carried the firearm on his or her person. (B) Penalty (i) In general Any person who violates subparagraph (A) shall be fined $500 per violation. (ii) Enhanced penalty If a person violates subparagraph (A) and a minor or a resident who is ineligible to possess a firearm under Federal, State, or local law obtains the firearm and causes injury or death to such minor or resident, or to any other individual, the person shall be fined under this title, imprisoned for not more than 5 years, or both. (iii) Forfeiture of improperly stored firearm Any firearm stored in violation of subparagraph (A) shall be subject to seizure and forfeiture in accordance with the procedures described in section 924(d). (C) Minor defined In this paragraph, the term minor means an individual who is less than 18 years of age. .\n#### 4. Firearm Safe Storage Program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Firearm Safe Storage Program 3061. Firearm Safe Storage Program (a) In general The Assistant Attorney General shall make grants to an eligible State or Indian Tribe to assist the State or Indian Tribe in carrying out the provisions of any State or Tribal law that is functionally identical to section 922(z)(4) of title 18, United States Code. (b) Eligible State or Indian Tribe (1) In general Except as provided in paragraph (2), a State or Indian Tribe shall be eligible to receive grants under this section on and after the earliest date as of which\u2014 (A) the State or Indian Tribe has enacted a law that is functionally identical to section 922(z)(4) of title 18, United States Code; and (B) the attorney general of the State (or comparable Tribal official) has submitted a written certification to the Assistant Attorney General stating that the law of the State or Indian Tribe reflects the sense of Congress in section 922(z)(4)(D) of such title 18. (2) First year eligibility exception (A) In general A covered State or Indian Tribe shall be eligible to receive a grant under this section during the 1-year period beginning on the date of enactment of this part. (B) Covered State or Indian Tribe In this paragraph, the term covered State or Indian Tribe means a State or Indian Tribe that, before the date of enactment of this part, enacted a law\u2014 (i) that is functionally identical to section 922(z)(4) of title 18, United States Code; and (ii) for which the attorney general of the State (or comparable Tribal official) submits a written certification to the Assistant Attorney General stating that the law of the State or Indian Tribe reflects the sense of Congress in section 922(z)(4)(D) of such title 18. (c) Use of funds Funds awarded under this section may be used by a State or Indian Tribe to assist law enforcement agencies or the courts of the State or Indian Tribe in enforcing and otherwise facilitating compliance with any State or Tribal law functionally identical to section 922(z)(4) of title 18, United States Code. (d) Application An eligible State or Indian Tribe desiring a grant under this section shall submit to the Assistant Attorney General an application at such time, in such manner, and containing or accompanied by such information, as the Assistant Attorney General may reasonably require. (e) Incentives For each of fiscal years 2025 through 2029, the Attorney General shall give affirmative preference to all Bureau of Justice Assistance discretionary grant applications of a State or Indian Tribe that has enacted a law\u2014 (1) functionally identical to section 922(z)(4) of title 18, United States Code; and (2) for which the attorney general of the State (or comparable Tribal official) submits a written certification to the Assistant Attorney General stating that the law of the State or Indian Tribe reflects the sense of Congress in section 922(z)(4)(D) of such title 18. .\n#### 5. Sense of Congress\nParagraph (4) of section 922(z) of title 18, United States Code, as added by section 3, is amended by adding at the end the following:\n(D) Sense of Congress relating to liability It is the sense of Congress that\u2014 (i) failure to comply with subparagraph (A) constitutes negligence under any relevant statute or common law rule; and (ii) when a violation of subparagraph (A) is the but-for cause of a harm caused by the discharge of a firearm, such violation should be deemed to be the legal or proximate cause of such harm, regardless of whether such harm was also the result of an intentional tort. .\n#### 6. Severability\nIf any provision of this Act, or an amendment made by this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act, or an amendment made by this Act, or the application of such provision to other persons or circumstances, shall not be affected.",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1564",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ethan's Law",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-07-24T14:08:23Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-24T14:08:23Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-24T14:08:23Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-24T14:08:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T16:08:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s726",
          "measure-number": "726",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s726v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ethan's Law</strong></p> <p>This bill establishes a framework to regulate the storage of firearms on residential premises at the federal, state, and tribal levels.</p> <p>At the federal level, the bill establishes statutory requirements for firearms on residential premises to be safely stored if a minor is likely to gain access without permission or if a resident is ineligible to possess a firearm.</p> <p>An individual who violates the requirements is subject to criminal penalties. A firearm stored in violation of the requirements is subject to seizure and forfeiture.</p> <p>At the state and tribal levels, the bill requires the Department of Justice to award grants to implement functionally identical requirements for the safe storage of firearms. </p>"
        },
        "title": "Ethan's Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s726.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ethan's Law</strong></p> <p>This bill establishes a framework to regulate the storage of firearms on residential premises at the federal, state, and tribal levels.</p> <p>At the federal level, the bill establishes statutory requirements for firearms on residential premises to be safely stored if a minor is likely to gain access without permission or if a resident is ineligible to possess a firearm.</p> <p>An individual who violates the requirements is subject to criminal penalties. A firearm stored in violation of the requirements is subject to seizure and forfeiture.</p> <p>At the state and tribal levels, the bill requires the Department of Justice to award grants to implement functionally identical requirements for the safe storage of firearms. </p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s726"
    },
    "title": "Ethan's Law"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ethan's Law</strong></p> <p>This bill establishes a framework to regulate the storage of firearms on residential premises at the federal, state, and tribal levels.</p> <p>At the federal level, the bill establishes statutory requirements for firearms on residential premises to be safely stored if a minor is likely to gain access without permission or if a resident is ineligible to possess a firearm.</p> <p>An individual who violates the requirements is subject to criminal penalties. A firearm stored in violation of the requirements is subject to seizure and forfeiture.</p> <p>At the state and tribal levels, the bill requires the Department of Justice to award grants to implement functionally identical requirements for the safe storage of firearms. </p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s726"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s726is.xml"
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
      "title": "Ethan's Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ethan's Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 44 of title 18, United States Code, to require the safe storage of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:23Z"
    }
  ]
}
```
