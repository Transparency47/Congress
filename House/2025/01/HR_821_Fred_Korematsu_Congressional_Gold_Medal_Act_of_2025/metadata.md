# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/821
- Title: Fred Korematsu Congressional Gold Medal Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 821
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-01-13T09:05:19Z
- Update date including text: 2026-01-13T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-28 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/821",
    "number": "821",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fred Korematsu Congressional Gold Medal Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:19Z",
    "updateDateIncludingText": "2026-01-13T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:11:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-28T16:11:15Z",
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
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "HI"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "UT"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
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
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WA"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "UT"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MD"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "OR"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
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
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr821ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 821\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Takano (for himself, Mr. Fong , Ms. Tokuda , Ms. Maloy , Ms. Matsui , and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo award posthumously a Congressional Gold Medal to Fred Korematsu, in recognition of his contributions to civil rights, his loyalty and patriotism to the Nation, and his dedication to justice and equality.\n#### 1. Short title\nThis Act may be cited as the Fred Korematsu Congressional Gold Medal Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nOn January 30, 1919, Fred Toyosaburo Korematsu was born in Oakland, California, to Japanese immigrants.\n**(2)**\nFred Korematsu graduated from Castlemont High School in 1937 and attempted to enlist in the military twice but was unable to do so because his selective service classification was changed to enemy alien, even though Fred Korematsu was a United States citizen.\n**(3)**\nFred Korematsu trained as a welder and worked as a foreman at the docks in Oakland until the date on which he and all Japanese Americans were fired.\n**(4)**\nOn December 7, 1941, Japan attacked the military base in Pearl Harbor, Hawaii, causing the United States to declare war against Japan.\n**(5)**\nOn February 19, 1942, President Franklin D. Roosevelt signed Executive Order 9066 (7 Fed. Reg. 1407 (February 25, 1942)), which authorized the Secretary of War to prescribe military areas\u2014\n**(A)**\nfrom which any or all people could be excluded; and\n**(B)**\nwith respect to which, the right of any person to enter, remain in, or leave would be subject to any restriction the Military Commander imposed in his discretion.\n**(6)**\nOn May 3, 1942, the Lieutenant General of the Western Command of the Army issued Civilian Exclusion Order 34 (May 3, 1942) (referred to in this preamble as the Civilian Exclusion Order ) directing that all people of Japanese ancestry be removed from designated areas of the West Coast after May 9, 1942, because people of Japanese ancestry in the designated areas were considered to pose a threat to national security.\n**(7)**\nFred Korematsu refused to comply with the Civilian Exclusion Order and was arrested on May 30, 1942.\n**(8)**\nAfter his arrest, Fred Korematsu\u2014\n**(A)**\nwas held for 2\u00bd months in the Presidio stockade in San Francisco, California;\n**(B)**\nwas convicted on September 8, 1942, of violating the Civilian Exclusion Order and sentenced to 5 years of probation; and\n**(C)**\nwas detained at Tanforan Assembly Center, a former horse racetrack used as a holding facility for Japanese Americans before he was exiled with his family to the Topaz incarceration camp in the State of Utah.\n**(9)**\nMore than 120,000 Japanese Americans were similarly detained, with no charges brought and without due process, in 10 permanent War Relocation Authority camps located in isolated desert areas of the States of Arizona, Arkansas, California, Colorado, Idaho, Utah, and Wyoming.\n**(10)**\nThe people of the United States subject to the Civilian Exclusion Order lost their homes, livelihoods, and the freedoms guaranteed to all people of the United States.\n**(11)**\nFred Korematsu unsuccessfully challenged the Civilian Exclusion Order as it applied to him and appealed the decision of the United States District Court to the United States Court of Appeals for the Ninth Circuit, which sustained his conviction.\n**(12)**\nFred Korematsu was subsequently confined with his family in the incarceration camp in Topaz, Utah, for 2 years, and during that time, Fred Korematsu appealed his conviction to the Supreme Court of the United States.\n**(13)**\nOn December 18, 1944, the Supreme Court of the United States issued Korematsu v. United States, 323 U.S. 214 (1944), which\u2014\n**(A)**\nupheld the conviction of Fred Korematsu by a vote of 6 to 3; and\n**(B)**\nconcluded that Fred Korematsu was removed from his home not based on hostility toward him or other Japanese Americans but because the United States was at war with Japan and the military feared a Japanese invasion of the West Coast.\n**(14)**\nIn his dissenting opinion in Korematsu v. United States, 323 U.S. 214 (1944), Justice Frank Murphy called the Civilian Exclusion Order the legalization of racism .\n**(15)**\nTwo other Supreme Court Justices dissented from the majority decision in Korematsu v. United States, including Justice Robert H. Jackson who described the validation of the principle of racial discrimination as a loaded weapon, ready for the hand of any authority that can bring forward a plausible claim of an urgent need .\n**(16)**\nFred Korematsu continued to maintain his innocence for decades following World War II, and his conviction hampered his ability to gain employment.\n**(17)**\nIn 1982, legal historian Peter Irons and researcher Aiko Yoshinaga-Herzig gained access to Government documents under section 552 of title 5, United States Code (commonly known as the Freedom of Information Act ), that indicate that while the case of Fred Korematsu was before the Supreme Court of the United States, the Federal Government misled the Supreme Court of the United States and suppressed findings that Japanese Americans on the West Coast were not security threats.\n**(18)**\nIn light of the newly discovered information, Fred Korematsu filed a writ of error coram nobis with the United States District Court for the Northern District of California, and on November 10, 1983, United States District Judge Marilyn Hall Patel issued her decision in Korematsu v. United States, 584 F. Supp. 1406 (N.D. Cal. 1984), that\u2014\n**(A)**\noverturned the Federal conviction of Fred Korematsu;\n**(B)**\nconcluded that, at the time that senior Government officials presented their case before the Supreme Court of the United States in 1944, the senior Government officials knew there was no factual basis for the claim of military necessity for the Civil Exclusion Order;\n**(C)**\nacknowledged that the government knowingly withheld information from the courts when they were considering the critical question of military necessity in the original case;\n**(D)**\nrecognized that there is substantial support in the record that the government deliberately omitted relevant information and provided misleading information in papers before the court. The information was critical to the court\u2019s determination ; and\n**(E)**\nstated that although the decision of the Supreme Court of the United States in Korematsu v. United States, 323 U.S. 214 (1944), remains on the pages of United States legal and political history, [a]s historical precedent it stands as a constant caution that in times of war or declared military necessity our institutions must be vigilant in protecting constitutional guarantees .\n**(19)**\nThe Commission on Wartime Relocation and Internment of Civilians, authorized by Congress in 1980 to review the facts and circumstances surrounding the relocation and incarceration of Japanese Americans under Executive Order 9066 (7 Fed. Reg. 1407 (February 25, 1942)), concluded that\u2014\n**(A)**\nthe decision of the Supreme Court of the United States in Korematsu v. United States, 323 U.S. 214 (1944), is overruled by the court of history;\n**(B)**\na grave personal injustice was done to the United States citizens and resident aliens of Japanese ancestry who, without individual review or any probative evidence against them, were excluded, removed, and detained by the United States during World War II; and\n**(C)**\nthe exclusion, removal, and detention of United States citizens and resident aliens of Japanese ancestry was motivated largely by racial prejudice, wartime hysteria, and a failure of political leadership .\n**(20)**\nThe overturning of the conviction of Fred Korematsu and the findings of the Commission on Wartime Relocation and Internment of Civilians influenced the decision by Congress to pass the Civil Liberties Act of 1988 ( 50 U.S.C. 4211 et seq. ) to request a Presidential apology and the symbolic payment of compensation to people of Japanese ancestry who lost liberty or property due to discriminatory actions of the Federal Government.\n**(21)**\nOn August 10, 1988, President Reagan signed the Civil Liberties Act of 1988 ( 50 U.S.C. 4211 et seq. ), stating, [H]ere we admit a wrong; here we reaffirm our commitment as a nation to equal justice under the law. .\n**(22)**\nOn January 15, 1998, President Clinton awarded the Presidential Medal of Freedom, the highest civilian award of the United States, to Fred Korematsu, stating, [i]n the long history of our country\u2019s constant search for justice, some names of ordinary citizens stand for millions of souls: Plessy, Brown, Parks. To that distinguished list, today we add the name of Fred Korematsu. .\n**(23)**\nFred Korematsu remained a tireless advocate for civil liberties and justice throughout his life by\u2014\n**(A)**\nspeaking out against racial discrimination and violence; and\n**(B)**\ncautioning the Federal Government against repeating mistakes of the past that singled out individuals for heightened scrutiny on the basis of race, ethnicity, nationality, or religion.\n**(24)**\nOn March 30, 2005, Fred Korematsu died at the age of 86 in Marin County, California.\n**(25)**\nFred Korematsu is a role model for all people of the United States who love the United States and the promises contained in the Constitution of the United States, and the strength and perseverance of Fred Korematsu serve as an inspiration for all people who strive for equality and justice.\n#### 3. Congressional gold medal\n##### (a) Presentation Authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the posthumous presentation, on behalf of Congress, of a gold medal of appropriate design in commemoration to Fred Korematsu, in recognition of his contributions to civil rights, his loyalty and patriotism to the Nation, and his dedication to justice and equality.\n##### (b) Design and Striking\nFor the purposes of the presentation referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions to be determined by the Secretary. The design shall bear an image of, and inscription of the name of, Fred Korematsu .\n##### (c) Smithsonian Institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the Smithsonian Institution, where it shall be available for display as appropriate and made available for research.\n**(2) Sense of Congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal awarded pursuant to this Act available for display elsewhere, particularly at the National Portrait Gallery, and that preference should be given to locations affiliated with the Smithsonian Institution.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck pursuant to section 3, at a price sufficient to cover the cost thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nThe medals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic Items\nFor purposes of sections 5134 and 5136 of title 3, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "338",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fred Korematsu Congressional Gold Medal Act of 2025",
      "type": "S"
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
            "name": "Asia",
            "updateDate": "2025-04-01T15:15:30Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "Smithsonian Institution",
            "updateDate": "2025-04-01T15:15:29Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-04-01T15:15:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-01T15:01:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr821",
          "measure-number": "821",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr821v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fred Korematsu Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal posthumously to Fred Korematsu in recognition of his contributions to civil rights, his loyalty and patriotism to the nation, and his dedication to justice and equality.</p>"
        },
        "title": "Fred Korematsu Congressional Gold Medal Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr821.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fred Korematsu Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal posthumously to Fred Korematsu in recognition of his contributions to civil rights, his loyalty and patriotism to the nation, and his dedication to justice and equality.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr821"
    },
    "title": "Fred Korematsu Congressional Gold Medal Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fred Korematsu Congressional Gold Medal Act of 2025</strong></p><p>This bill provides for the award of a Congressional Gold Medal posthumously to Fred Korematsu in recognition of his contributions to civil rights, his loyalty and patriotism to the nation, and his dedication to justice and equality.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr821"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr821ih.xml"
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
      "title": "Fred Korematsu Congressional Gold Medal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:06Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award posthumously a Congressional Gold Medal to Fred Korematsu, in recognition of his contributions to civil rights, his loyalty and patriotism to the Nation, and his dedication to justice and equality.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:03:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fred Korematsu Congressional Gold Medal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:53:20Z"
    }
  ]
}
```
