# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2195
- Title: WWII Nurses Congressional Gold Medal Act
- Congress: 119
- Bill type: S
- Bill number: 2195
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2195",
    "number": "2195",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "WWII Nurses Congressional Gold Medal Act",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
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
            "date": "2025-06-26T21:31:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-26T21:31:15Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NM"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "NV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "IN"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "NE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "RI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CO"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "DE"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2195is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2195\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Ms. Baldwin (for herself, Mr. Daines , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo award a Congressional Gold Medal, collectively, to the brave women who served in World War II as members of the U.S. Army Nurse Corps and U.S. Navy Nurse Corps.\n#### 1. Short title\nThis Act may be cited as the WWII Nurses Congressional Gold Medal Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nOn December 8, 1941, the United States declared war against the Empire of Japan, followed by declarations of war against Germany and Italy on December 11, 1941. In 1935, there were fewer than 600 United States Army nurses and 1,700 United States Navy nurses on active duty. By the time World War II ended, more than 59,000 Army nurses and 14,000 Navy nurses had volunteered to serve.\n**(2)**\nThe Act of June 4, 1920 (41 Stat. 759; chapter 227), granted women in the Nurse Corps relative rank . This gave them the right to wear the military insignia, but did not confer military status or privileges. This arrangement meant women serving throughout World War II received 50 percent of the pay as compared to their male counterparts, and none of the veteran benefits. Because they did not receive military status, they received no orientation or training before being deployed to hospitals near the front lines.\n**(3)**\nNurses served under fire in field hospitals and evacuation hospitals across 6 continents, on hospital trains and ships, and as flight nurses on medical transport planes. Several nurses were killed in action when their ships were torpedoed or field hospitals were bombed. Some even entered into combat areas as flight nurses to retrieve the wounded, and 2 groups were captured as prisoners of war by the Japanese.\n**(4)**\nGeneral Douglas MacArthur ordered American and Filipino Army Corps nurses and other medical personnel to the Bataan Peninsula to prepare 2 emergency hospitals for United States and Filipino forces. General Hospital No. 1 received casualties directly from the front lines and occupied an old Army barracks in Limay, Bataan prior to implementation of War Plan Orange 3 on December 24, 1941. The hospital received more than 1,200 battle casualties requiring major surgery within a month. General Hospital No. 2, a makeshift open ward hospital, was set up in Cabcaben, Bataan to receive discharged patients from Hospital No. 1. Hospital No. 2 accepted patients strong enough for evacuation, as it was out in the open, with no tents or buildings, and only tree canopy to conceal them from Japanese aircraft. Due to constant bombing, Hospital No. 1 was transferred to Little Baguio in Mariveles, Bataan on January 25, 1942. Hospital No. 1 was bombed on March 29, 1942, and again on April 7, killing or wounding more than 100 patients, but the nurses carried on with their duties as well as they were able. Fifty-three American and 31 Filipina nurses were ordered to move from Bataan to Corregidor Island on April 8. Ten of the American nurses were transferred successfully to Australia prior to the fall of Corregidor on May 6, 1942. Sixty-seven American nurses were eventually moved to Santo Tomas University Internment Camp where they were liberated in February 1945 while 31 Filipina nurses were moved to Bilibid Prison where they were conditionally released in July 1942.\n**(5)**\nOn December 10, 1941, Sangley Point Navy Yard was bombed by Japanese planes. American and Filipino Navy Corps nurses, medical personnel and patients of Ca\u00f1acao Naval Hospital were transferred to the Army Sternberg Hospital in Manila. During the first week of January 1942, the Japanese Army occupied Manila and the Navy nurses were transferred to St. Scholastica\u2019s College with their patients and eventually to Santo Tomas University Internment Camp on March 12, 1942. Eleven American and Filipino Navy Corps nurses were transferred to Los Ba\u00f1os Prison Camp on May 14, 1943, where they stayed until their liberation in February 1945. Following the United States Army surrender of the Philippines to the Japanese on May 6, 1942, 67 Army nurses were taken to Santo Tomas Internment Camp in Manila, where they remained until February 1945. During the 37 months in captivity, these women endured primitive conditions and starvation rations, but continued to care for the ill and injured in the internment camp hospital.\n**(6)**\nChinese, Chinese-American, and Japanese-American nurses served in Army Hospitals in China, Hawaii, and in the mainland United States under the Army and Navy Corps. Despite the internment of many Japanese-American families during World War II, Japanese-American women joined the Nurse Cadet Corps to serve the United States. Chinese and Chinese-American nurses were recruited by the Flying Tigers, serving both in dangerous missions over the Himalayas as well as in U.S. Army hospitals.\n**(7)**\nEarly in the morning of November 8, 1942, 60 nurses attached to the 48th Surgical Hospital landed off the coast of North Africa. The nurses wore helmets and carried full packs containing medical equipment. Without weapons, they waded ashore amid enemy sniper fire and ultimately took shelter in an abandoned civilian hospital, where they began caring for invasion casualties. There was no electricity or running water, and the only medical supplies available were those the nurses had brought themselves.\n**(8)**\nIn Anzio, Italy, nurses dug foxholes outside their tents or under their cots and cared for patients under German shellfire. The field hospital tents were marked by large red crosses and were sometimes deliberately hit with artillery shells and bombs. On February 7, 1944, a German pilot being pursued by British fighter planes dropped 5 antipersonnel bombs on the hospital, destroying 29 ward tents, killing 26 and wounding 64. The dead included 3 nurses, 2 medical officers, a Red Cross worker, 14 enlisted men and 6 patients. Troops came to refer to the hospital area as Hell\u2019s Half-Acre because it was hit so frequently by enemy fire. At least 200 nurses took part in the Anzio campaign, caring for more than 33,000 patients behind enemy lines.\n**(9)**\nArmy and Navy nurses acclimated quickly to difficult and dangerous conditions with a minimum of complaints, and were essential members of the field armies.\n**(10)**\nThe presence of nurses at the front improved morale because soldiers realized that they would receive skilled care in the event they were wounded.\n**(11)**\nThanks largely to the efforts of these nurses, fewer than 4 percent of the American soldiers who received medical care in the field or underwent evacuation died from wounds or disease.\n**(12)**\nAfter the war, broad public health missions required that Army and Navy nurses supervise communicable disease measures as former enemy countries were reorganized. In Hiroshima, these officers cared for victims of the atomic bombs. In Munich, they prevented mass epidemic in refugee camps. Army and Navy nurses even provided prenatal, infant, and mental health care in other former-enemy territories.\n**(13)**\nNurses received 1,619 medals, citations, and commendations during the war, reflecting the courage and dedication of all who served. Sixteen medals were awarded posthumously to nurses who died as a result of enemy fire, including 6 nurses who died at Anzio, 6 who died when the hospital ship Comfort was attacked by a Japanese suicide plane, and 4 flight nurses. Thirteen other flight nurses died in weather-related crashes while on duty.\n**(14)**\nIn 1944, Congress passed a bill that granted Army and Navy Nurses actual military rank and benefits, approved for the duration of the war plus 6 months.\n**(15)**\nIn 1947, Congress passed legislation establishing a permanent Army and Navy Nursing Corps and gave members permanent officer status with equal pay and the same benefits as those given to male officers.\n**(16)**\nIn 1948, all military branches were integrated and female doctors were finally admitted to the Army Medical Corps.\n**(17)**\nAlthough African-American nurses were fully qualified and prepared to serve as nurses at the onset of World War II, racial segregation and discrimination made it difficult for Black women to join the ranks of the Army Nurse Corps.\n**(18)**\nAs the Army Nurse Corps began expanding its recruiting process, thousands of Black nurses who wanted to serve their country filled out applications.\n**(19)**\nWhile the Army did eventually integrate African-American nurses in 1941, it did so unwillingly and placed a quota on the number of African-American nurses that they would accept, capping the number allowed to join at 56.\n**(20)**\nMany of them had hardship tours and were sent to segregated camps to take care of African-American soldiers and would rotate and allow White nurses reprieve in taking care of German prisoners of war. As the war progressed, the number of Black nurses allowed to enlist remained low, although the quota was officially lifted in July 1944.\n**(21)**\nThe extraordinary efforts of these women are deserving of belated official recognition.\n**(22)**\nThe United States is eternally grateful to the nurses of the Army and Navy Nurse Corps for their bravery and dedication to their patients through World War II, which saved lives and made significant contributions to the defeat of the Axis powers.\n#### 3. Congressional gold medal\n##### (a) Award authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the award, on behalf of Congress, of a gold medal of appropriate design in honor of World War II Army and Navy Nurse Corps members, in recognition of the critical military service and devotion to duty of those nurses.\n##### (b) Design and striking\nFor purposes of the award described in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike the gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian Institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the Smithsonian Institution, where it shall be available for display as appropriate and made available for research.\n**(2) Sense of Congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal received under paragraph (1) available for display elsewhere, particularly at\u2014\n**(A)**\nappropriate locations associated with the Army and Navy Nurse Corps of World War II, including\u2014\n**(i)**\nthe U.S. Army Medical Center of Excellence;\n**(ii)**\nthe Women in Military Service for America Memorial;\n**(iii)**\nthe U.S. Army Women\u2019s Museum;\n**(iv)**\nthe National Naval Medical Centers; and\n**(v)**\nthe National World War II Museum; and\n**(B)**\nany other location determined appropriate by the Smithsonian Institution.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs of the medals, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nMedals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4901",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "WWII Nurses Congressional Gold Medal Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-07T17:06:02Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2195is.xml"
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
      "title": "WWII Nurses Congressional Gold Medal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WWII Nurses Congressional Gold Medal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to award a Congressional Gold Medal, collectively, to the brave women who served in World War II as members of the U.S. Army Nurse Corps and U.S. Navy Nurse Corps.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:33:24Z"
    }
  ]
}
```
