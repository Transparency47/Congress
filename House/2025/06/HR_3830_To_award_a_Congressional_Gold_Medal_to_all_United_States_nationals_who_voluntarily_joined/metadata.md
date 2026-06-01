# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3830?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3830
- Title: American Patriots of WWII through Service with the Canadian and British Armed Forces Gold Medal Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3830
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2026-01-22T09:06:06Z
- Update date including text: 2026-01-22T09:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3830",
    "number": "3830",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "American Patriots of WWII through Service with the Canadian and British Armed Forces Gold Medal Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T09:06:06Z",
    "updateDateIncludingText": "2026-01-22T09:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:00:40Z",
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
          "date": "2025-06-06T13:00:35Z",
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
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "MS"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3830ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3830\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Vindman (for himself and Mr. Kelly of Mississippi ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo award a Congressional Gold Medal to all United States nationals who voluntarily joined the Canadian and British Armed Forces and their supporting entities during World War II, in recognition of their dedicated service.\n#### 1. Short title\nThis Act may be cited as the American Patriots of WWII through Service with the Canadian and British Armed Forces Gold Medal Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAmericans from across the country served in defense of democracy and freedom during World War II (WWII) by volunteering for service with the Canadian and British militaries and other associated organizations that were fighting Nazi and Fascist aggression. Many United States citizens perceived the importance of this war and the severe impact Nazism and Fascism could have on the American way of life. Therefore, prior to the United States entry into the conflict and indeed throughout WWII these patriots independently crossed the border into Canada and entered Canadian and British Armed Forces recruiting offices or sought out representatives based in major United States municipalities and elsewhere.\n**(2)**\nWhen the United Kingdom of Great Britain and Northern Ireland and the British Commonwealth of Nations were drawn into WWII after Germany invaded Poland in 1939, the Canadian and British Air Forces made a concerted effort to recruit Americans.\n**(3)**\nIt is documented that thousands of Americans joined the Canadian and British Armed Forces, a large percentage joining the Royal Canadian Air Force (RCAF) alone. In a 1942 film Air Marshal William Avery Billy Bishop, an organizer and promoter of the British Commonwealth Air Training Plan (BCATP) and Director of the Royal Canadian Air Force, recognized the gallant lads from the United States who have come up here to help and serve with us . Notably, many Americans were also recruited and processed through Canada before being assigned to or detached for the purpose of Royal Air Force (RAF) service.\n**(4)**\nGeneral of the Army, Army of the United States, Dwight D. Eisenhower, the former Supreme Allied Commander of the Allied Expeditionary Force, referenced, in a speech on January 10, 1946, the some twelve thousand American citizens who crossed into Canada with the goal of entering the Canadian Armed Forces. Although the precise numbers of Americans who were in Canadian and British service are unknown, media accounts published by Allied journalists during the conflict nonetheless detail their legacies of volunteerism, personal sacrifice, and bravery.\n**(5)**\nAmericans also joined the Canadian Aviation Bureau, and the Home Guard, Air Transport Auxiliary (ATA), and Royal Air Force Ferry Command/Transport Command in Britain. The existence of these ancillaries enabled patriotic citizens, who were, at least initially, unable to join a branch of the United States military due to gender, age, race, health, the lack of sufficient college education, or other reasons, to support the war effort. Those who contributed via these alternative concerns were no less essential to attaining victory.\n**(6)**\nThe infusion of Americans into Canada helped to reduce shortages of civilian and military pilots in the BCATP, and President Franklin Roosevelt paid tribute to both Canada and the program in a wartime letter to Canadian Prime Minister William Lyon Mackenzie King. Within the correspondence President Roosevelt used the phrase the Aerodrome of Democracy .\n**(7)**\nAs members of the Canadian and British militaries, the American volunteers served in many capacities. Extant military rolls and individual service records document, and thereby testify to, their contributions.\n**(8)**\nA sizable number of Americans lost their lives or were wounded while serving in the RCAF and RAF. The Canadian Army, British Army, Royal Canadian Navy, and Royal Navy also incurred American personnel casualties. Those who perished and the survivors demonstrated the exceptional courage that has been repeatedly displayed in the defense of freedom throughout American history.\n**(9)**\nA unique and highly publicized group of Americans, who were members of the RCAF and RAF, were posted to the famous RAF Eagle Squadrons and thereby showcased the important roles American volunteers were undertaking. British Prime Minister Winston Churchill, whose mother was American, played an important role in originally promoting the concept of the Eagle Squadrons to the Air Ministry.\n**(10)**\nThe early successes of female ferry aircrews paved the way for the formation in the United States of the Women Airforce Service Pilots (WASP) in 1943. The exceptional legacy of the Women Airforce Service Pilots, ATA, etc., provided essential support and paved the way for future generations of military women.\n**(11)**\nA substantial portion of the Americans serving in Canadian and British aerial forces transferred to the United States Army Air Forces between 1942 and 1944, while others elected to enter other branches of the United States Military.\n**(12)**\nThe practical experience these veterans of Canadian and British service possessed provided the inexperienced American Forces with an immediate degree of competence and effectiveness. More than a few became accomplished combat pilots, the American Fighter Aces Association possessing many of them within the organization\u2019s core membership.\n**(13)**\nThe bravery and foresight displayed by the Americans who enlisted in the Canadian and British Armed Forces represent a largely unrecognized story of valor, and their initiatives are worthy of official recognition.\n**(14)**\nThe United States Nationals who volunteered for service with military-associated Canadian and British ancillary entities are to be equally recognized for their volunteerism, contributions, and sacrifices.\n#### 3. Congressional gold medal\n##### (a) Award authorized\nThe President pro tempore of the Senate and the Speaker of the House of Representatives shall make appropriate arrangements for the award, on behalf of Congress, of a single gold medal of appropriate design to all United States nationals who voluntarily joined the Canadian and British Armed Forces and their supporting entities during World War II, in recognition of their dedicated service.\n##### (b) Design and striking\nFor the purposes of the award referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike the gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the Smithsonian Institution, where it will be available for display as appropriate and made available for research.\n**(2) Sense of congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal received under paragraph (1) available for display elsewhere.\n##### (d) Duplicate medals\nUnder regulations that the Secretary may promulgate, the Secretary may strike and sell duplicates in bronze of the gold medal struck under this Act, at a price sufficient to cover the costs of the medals, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 4. Status of medals\n##### (a) National medals\nMedals struck under this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of section 5134 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.",
      "versionDate": "2025-06-06",
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
        "updateDate": "2025-07-17T20:27:21Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3830ih.xml"
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
      "title": "American Patriots of WWII through Service with the Canadian and British Armed Forces Gold Medal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T08:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Patriots of WWII through Service with the Canadian and British Armed Forces Gold Medal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T08:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional Gold Medal to all United States nationals who voluntarily joined the Canadian and British Armed Forces and their supporting entities during World War II, in recognition of their dedicated service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T08:04:15Z"
    }
  ]
}
```
