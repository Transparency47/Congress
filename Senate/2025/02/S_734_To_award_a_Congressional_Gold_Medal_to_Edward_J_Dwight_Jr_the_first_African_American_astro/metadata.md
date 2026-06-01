# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/734
- Title: Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 734
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/734",
    "number": "734",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
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
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
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
            "date": "2025-02-25T23:38:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-25T23:38:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s734is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 734\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Bennet (for himself, Mr. Cornyn , Mr. Hickenlooper , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo award a Congressional Gold Medal to Edward J. Dwight, Jr., the first African American astronaut candidate in the United States.\n#### 1. Short title\nThis Act may be cited as the Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEdward Joseph Dwight, Jr., was born on September 9, 1933, to Georgia Baker Dwight and Edward Dwight, Sr., in Kansas City, Kansas. Ed Senior had been a second baseman and center fielder for the Kansas City Monarchs and played on other all-Black teams from 1924 to 1937. Georgia was a devoted mother who enrolled her son in a Head Start type program at the age of 2 and made sure to expose her children to as much culture as she could.\n**(2)**\nEdward Joseph Dwight, Jr., grew up with a passion for art and airplanes.\n**(3)**\nEdward became the first African American male to graduate from Bishop Ward Catholic High School in 1951. He then earned an associate degree in engineering in 1953 from Kansas City Junior College. That same year he left to join the Air Force and began flight training.\n**(4)**\nAfter completing flight training, he served as a military pilot and obtained a degree in aeronautical engineering from Arizona State University. During his career as an officer in the Air Force, Edward served at bases in Texas, Missouri, and Arizona, developing technical manuals and training fellow pilots on various instruments, as he accumulated flight hours.\n**(5)**\nEdward recalled, I was the only Black officer pilot just about every base I was stationed and that even at 5\u20194\u201d, he got award after award . While in the Air Force, Edward earned his Bachelor of Science in aeronautical engineering from Arizona State University in 1957.\n**(6)**\nEdward flew some of the most advanced aircraft of the era and ultimately accumulated over 9,000 hours of flight time, 2,000 in high-performance jets. His engineering background and extensive training opened the door for him to enter the test pilot school where the most successful trainees become astronauts.\n**(7)**\nEdward was chosen by President John F. Kennedy to enter training as an experimental test pilot. The Kennedy administration knew that a Black astronaut would be an inspiring display of opportunity for African Americans across the country.\n**(8)**\nOn November 4, 1961, Edward received a letter inviting him to join the astronaut training program. He followed the advice of his mother and accepted the invitation to take the first steps toward improving diversity and talent in the United States space program by becoming the first African American astronaut candidate in the United States.\n**(9)**\nEdward went to the Aerospace Research Pilot School at Edwards Air Force Base in California to begin training.\n**(10)**\nThis was a time of uncertainty where the color of a person\u2019s skin mattered more than his or her skill.\n**(11)**\nThe astronaut candidacy of Edwards became cover news on Black magazines such as Jet, Ebony, and Sepia.\n**(12)**\nAt Edwards Air Force Base, however, Edward experienced prejudice and scorn, as he recounted in his autobiography Soaring on the Wings of a Dream: The Untold Story of America's First Black Astronaut Candidate .\n**(13)**\nEdward completed the experimental test pilot course and entered aerospace research pilot training in preparation for astronaut duties. He successfully completed the course and continued to perform duties as a fully qualified aerospace research pilot.\n**(14)**\nOn October 18, 1963, the National Aeronautics and Space Administration (referred to in this section as NASA ) announced 14 astronauts for Group 3, but Edward did not make the list.\n**(15)**\nWhile in training, Edward faced obstacles due to his race, which derailed his chance to be the first African American in space. His fight for equality was one of many trailblazing battles happening during the Civil Rights Era.\n**(16)**\nThe assassination of President Kennedy, the main sponsor in the White House of Edward and the space journey, led to his voluntary separation from the Air Force.\n**(17)**\nIn 1966, Edward resigned from the Air Force as a captain and moved to Denver, Colorado.\n**(18)**\nAfter the Kennedy assassination, pressure on NASA to fly a Black astronaut waned, and the first African American would not fly in space until Guion Bluford flew with the crew of NASA\u2019s eighth space flight on the Space Shuttle orbiter Challenger in 1983.\n**(19)**\nAfter successful careers in the Air Force, and as an IBM systems engineer, restauranteur, aviation consultant, real estate, and construction entrepreneur, Edward dedicated 43 years solely to his artistic endeavors.\n**(20)**\nIn 1974, George Brown, the first African American lieutenant governor of Colorado and a member of the Tuskegee Airmen in World War II, chose Edward to create a bronze bust of him to display in the Colorado State Capitol.\n**(21)**\nBeing a neophyte to bronze sculpting, and at the age of 42, Edward enrolled at the University of Denver in the Masters of Fine Arts program. While at the University of Denver, he became proficient in metal casting and managed the foundry at the school while also teaching other students. He received his Master of Fine Arts in 1977.\n**(22)**\nIn 1975, while at the University of Denver, Edward received a commission from the Colorado Centennial Commission to create a series of bronzes depicting the contribution of Blacks to the American Frontier West. The series exhibited for several years throughout the United States, gaining widespread acceptance and critical acclaim.\n**(23)**\nIn 1979, the National Park Service encouraged Edward to create a bronze series portraying the history and historical roots of jazz. The series was created and entitled Jazz: An American Art Form , which consisted of over 70 bronzes depicting the evolution of jazz from its African origins to the fusion of contemporary music.\n**(24)**\nSince his art career began in 1976, Edward has become one of most prolific and insightful sculptors in the United States. As of the date of enactment of this Act, Edward has completed more than 115 large-scale commissioned sculpture installations. His pieces are collected by museums, institutions and art enthusiasts around the world, including the Smithsonian. Ed Dwight Studios, Inc., in Denver, is now one of the largest privately owned production facilities in the western United States.\n**(25)**\nEdward is the recipient of numerable living legends awards from around the country for his achievements in space activities and contributions in art and Black history.\n**(26)**\nOn August 5, 2020, in recognition of his accomplishments as a scientist, test pilot, and sculptor, the Space Force inducted him as an honorary member. A permanent display is installed at the Pentagon in honor of these achievements.\n**(27)**\nIn a ceremony at the Pentagon, General Jay Raymond, Chief of Space Operations of the Space Force, presented Edward with the Commander\u2019s Public Service Award and inducted him as an honorary member of the Space Force, for his contributions to the United States, space, and history during times of overt racism in the field of science. Astronaut Victor Glover honored Edward by carrying this award with him to the International Space Station during his Crew-1 mission. Despite all that he had to overcome, Edward was an example of excellence, embarking on a nationwide speaking tour encouraging young people to study science, engineering, and math.\n**(28)**\nIn 2021, the Minor Planet Center, an organization affiliated with the International Astronomical Union, named an asteroid after Edward. NASA has honored him by sending his sculpture Pioneer Woman to space on Exploration Flight Test-1 in 2014.\n**(29)**\nOn November 3, 2022, Denver International Airport opened an exhibit titled Soaring on the Wings of a Dream, the title of Edward's book. The exhibit is on the life of Edward, beginning with childhood and ending with adulthood. It will be on display for 5 months.\n**(30)**\nThe National Geographic documentary, The Space Race , weaves together the stories of Black astronauts seeking to break the bonds of social injustice to reach for the stars, including Edward, Guion Bluford, Charles Bolden, Mae C. Jemison, Victor Glover, among many others, including Leland Melvin, one of the producers of the film.\n**(31)**\nOn May 19, 2024, Edward, sponsored by Space for Humanity, finally traveled to space as 1 of 6 individuals aboard the Blue Origin New Shepard rocket, which launched from a private site near Van Horn, Texas. At 90 years old, Edward became the oldest person to go to space.\n#### 3. Congressional Gold Medal\n##### (a) Presentation authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the presentation, on behalf of Congress, of a single gold medal of appropriate design to Edward J. Dwight, the first African-American astronaut candidate in the United States, in recognition of\u2014\n**(1)**\nhis historic service to the United States;\n**(2)**\nthe example of excellence during times of struggle and overt racism; and\n**(3)**\nhis contributions in art and Black history.\n##### (b) Design and striking\nFor purposes of the presentation described in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary. The design shall bear an image of, and an inscription of the name of, Edward J. Dwight, Jr.\n##### (c) Disposition of medal\nFollowing the presentation described in subsection (a), the gold medal shall be given to Edward J. Dwight, Jr., or, if unavailable, to Curtis Christopher Dwight.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nMedals struck under this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "1626",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Edward J. Dwight, Jr., Congressional Gold Medal Act of 2025",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-21T14:03:33Z"
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
          "measure-id": "id119s734",
          "measure-number": "734",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-08-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s734v00",
            "update-date": "2025-08-06"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Edward J. Dwight, Jr., Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal to Edward J. Dwight, Jr., the first African American astronaut candidate in the United States, in recognition of his historic service to the United States, his example of excellence during times of struggle and overt racism, and his contributions in art and Black history.\u00a0</p>"
        },
        "title": "Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s734.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Edward J. Dwight, Jr., Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal to Edward J. Dwight, Jr., the first African American astronaut candidate in the United States, in recognition of his historic service to the United States, his example of excellence during times of struggle and overt racism, and his contributions in art and Black history.\u00a0</p>",
      "updateDate": "2025-08-06",
      "versionCode": "id119s734"
    },
    "title": "Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Edward J. Dwight, Jr., Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal to Edward J. Dwight, Jr., the first African American astronaut candidate in the United States, in recognition of his historic service to the United States, his example of excellence during times of struggle and overt racism, and his contributions in art and Black history.\u00a0</p>",
      "updateDate": "2025-08-06",
      "versionCode": "id119s734"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s734is.xml"
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
      "title": "Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Edward J. Dwight, Jr. Congressional Gold Medal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to award a Congressional Gold Medal to Edward J. Dwight, Jr., the first African American astronaut candidate in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:30Z"
    }
  ]
}
```
