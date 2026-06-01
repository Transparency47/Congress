# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5934?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5934
- Title: Major Thomas D. Howie Congressional Gold Medal
- Congress: 119
- Bill type: HR
- Bill number: 5934
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2026-02-25T09:06:38Z
- Update date including text: 2026-02-25T09:06:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5934",
    "number": "5934",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001325",
        "district": "3",
        "firstName": "Sheri",
        "fullName": "Rep. Biggs, Sheri [R-SC-3]",
        "lastName": "Biggs",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Major Thomas D. Howie Congressional Gold Medal",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:38Z",
    "updateDateIncludingText": "2026-02-25T09:06:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "GA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "MD"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "LA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "GA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "SC"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5934ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5934\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mrs. Biggs of South Carolina (for herself, Ms. Mace , Mr. Wilson of South Carolina , Mr. Fry , Mr. Timmons , Mr. McCormick , Mr. Cline , Mr. Stanton , Mr. Harris of Maryland , Mr. Van Drew , Mr. Higgins of Louisiana , Mr. Lawler , Mr. Carter of Georgia , Mr. Tiffany , Mr. Veasey , Mr. Obernolte , Mr. Griffith , and Mr. Gooden ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo award a Congressional gold medal to Major Thomas D. Howie, in recognition of his bravery and outstanding service during the Battle of Normandy.\n#### 1. Short title\nThis Act may be cited as the Major Thomas D. Howie Congressional Gold Medal .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMajor Thomas D. Howie was born on April 12, 1908, in Abbeville, South Carolina, and went on to both a storied academic and athletic career at The Citadel as class president, a star football halfback, and captain of the baseball team.\n**(2)**\nMajor Howie answered his nations call to service by accepting a commission as a Second Lieutenant in the Officers Reserve Corps in the Virginia National Guard upon graduation from The Citadel.\n**(3)**\nMajor Howie was commissioned into the U.S. Army Reserve and later transferred to the Virginia National Guard\u2019s 116th Infantry Regiment in Staunton, Virginia.\n**(4)**\nMajor Thomas Howie valiantly served his country during the Battle of Normandy, demonstrating exceptional courage, devotion to duty, and skill in battle after landing on Omaha Beach on June 6, 1944.\n**(5)**\nMajor Howie commanded 3rd Battalion, 116th Infantry Regiment, 29th Infantry Division on July 13, 1944, and shortly thereafter was tasked with rescuing the encircled 2nd Battalion, 116th Infantry Regiment.\n**(6)**\nMajor Howie was instructed by his commanding officer to take St. Lo on July 17, 1944, he decided to leave the battered 2nd Battalion behind to recuperate and proceed with only the 3rd Battalion. When questioned on this, he was overheard saying See you in St. Lo to Major General Charles Gerhardt, words which would serve as inspiration for his men in the coming battle.\n**(7)**\nWhile giving his company commanders instructions for the attack, the unit came under fire from German mortars, and Major Howie was killed, a sacrifice for which he was posthumously awarded a Silver Star, Bronze Star, Purple Heart, French Legion of Honor, French Fourragere, and Combat Infantry Badge.\n**(8)**\nMajor Howie\u2019s men strapped his body to a stretcher, draped him with an American flag, and placed him on the hood of a Jeep so that he could be the first American to enter St. Lo. He was laid in the rubble of the St. Croix Cathedral, where fellow soldiers and French civilians paid their respects. From then on, he was known as The Major of St. Lo .\n**(9)**\nMajor Howie\u2019s leadership and unwavering commitment to his soldiers inspired bravery and determination among his troops, ultimately leading to the successful capture of St. Lo, a crucial strategic objective that directly led to Operation Cobra and the Allied Liberation France, Belgium, and the Netherlands from Nazi Tyranny.\n**(10)**\nThough his command of the 116th Infantry Regiment was short-lived, Major Howie embodied the extraordinary courage and valor that defined American soldiers during the Battle of Normandy. His sacrifice echoes through the halls of history to inspire Americans to this day.\n**(11)**\nThe character of Major Howie was used as inspiration for the role of Captain John Miller, portrayed by Tom Hanks in the movie Saving Private Ryan . This brought attention to his remarkable leadership and sacrifice, thereby furthering public recognition of his valor.\n**(12)**\nMajor Howie\u2019s legacy extends beyond the silver screen. Monuments and markers commemorating his valor and leadership stand in Abbeville, Greenwood, and Charleston, South Carolina; Staunton, Virginia; Shelby, North Carolina; and Saint-Lo, Normandy, France. In 2003, South Carolina further honored him with a posthumous induction into the South Carolina Hall of Fame.\n**(13)**\nMajor Howie\u2019s sacrifice and exemplary service symbolize the highest ideals of patriotism, integrity, and dedication to duty.\n**(14)**\nMajor Thomas D. Howie\u2019s legacy continues to inspire future generations to uphold the seven army values of loyalty, duty, respect, selfless service, honor, integrity, and personal courage.\n#### 3. Congressional gold medal\n##### (a) Award authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the posthumous award, on behalf of Congress, of a gold medal of appropriate design to Major Thomas D. Howie, in recognition of his bravery and outstanding service during the Battle of Normandy.\n##### (b) Design and striking\nFor the purpose of the award referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions to be determined by the Secretary.\n##### (c) Presentation\nThe gold medal referred to in subsection (a) shall be presented to\u2014\n**(1)**\nthe nephew of Thomas Howie, Tom Howie; or\n**(2)**\nif Tom Howie is unavailable, the next of kin of Thomas Howie.\n##### (d) Award of medal\nFollowing the presentation described in subsection (c), the gold medal shall be given to The Citadel Museum, where it shall be displayed as appropriate and made available for research.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs of such medals, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nThe medals struck under this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck pursuant to this Act.\n##### (b) Proceeds of sale\nThe amounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:59:43Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5934ih.xml"
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
      "title": "Major Thomas D. Howie Congressional Gold Medal",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Major Thomas D. Howie Congressional Gold Medal",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional gold medal to Major Thomas D. Howie, in recognition of his bravery and outstanding service during the Battle of Normandy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:50:22Z"
    }
  ]
}
```
