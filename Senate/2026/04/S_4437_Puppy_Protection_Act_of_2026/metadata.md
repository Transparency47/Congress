# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4437
- Title: Puppy Protection Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4437
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-19T21:20:31Z
- Update date including text: 2026-05-19T21:20:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2131)
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2131)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4437",
    "number": "4437",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Puppy Protection Act of 2026",
    "type": "S",
    "updateDate": "2026-05-19T21:20:31Z",
    "updateDateIncludingText": "2026-05-19T21:20:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2131)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-29",
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
        "item": {
          "date": "2026-04-29T20:32:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-29",
      "state": "VT"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NV"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4437is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4437\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Durbin (for himself, Mr. Schiff , Mrs. Gillibrand , Ms. Alsobrooks , Mr. Merkley , Mr. Booker , Ms. Smith , Mr. Van Hollen , Ms. Duckworth , Mr. Hickenlooper , Mr. Sanders , Mr. Warner , Mr. Coons , Mr. Blumenthal , Mr. Wyden , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Animal Welfare Act to establish additional requirements for dealers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Puppy Protection Act of 2026 .\n#### 2. Additional requirements for dealers\n##### (a) Humane treatment of dogs by dealers\nSection 13(a) of the Animal Welfare Act ( 7 U.S.C. 2143(a) ) is amended by adding at the end the following:\n(9) In addition to the requirements under paragraph (2), the standards described in paragraph (1) shall, with respect to dealers, include requirements\u2014 (A) that the dealer provide adequate housing for dogs that includes\u2014 (i) completely solid flooring; (ii) indoor space sufficient to allow the tallest dog in an enclosure to stand on his or her hind legs without touching the roof of the enclosure; (iii) with respect to dogs over 8 weeks in age, primary enclosures that, with the length of the dog measured from the tip of the nose to the base of the tail, provide at least\u2014 (I) 12 square feet of indoor floor space per each dog measuring not more than 25 inches long; (II) 20 square feet of indoor floor space per each dog measuring more than 25 but less than 35 inches long; and (III) 30 square feet of indoor floor space per each dog measuring not less than 35 inches long; (iv) enclosures that are not stacked or otherwise placed on top of or below another enclosure; and (v) temperature control that\u2014 (I) is appropriate for the age, breed, and condition of each dog in the enclosure; and (II) is between 45 and 85 degrees Fahrenheit, when dogs are present in the enclosure; (B) that appropriate and nutritious food be provided to each dog at least twice per day, in an amount sufficient to maintain the good health and physical condition of each dog; (C) that each dog has continuous access to potable water that is not frozen and is free of feces, algae, and other contaminants; (D) that each dog has adequate exercise, including, for each dog over the age of 12 weeks\u2014 (i) except as provided in clause (ii), unrestricted access from the primary enclosure of the dog during daylight hours to an outdoor exercise area that\u2014 (I) is at ground-level; (II) is a solid surface; (III) is enclosed by a fence or other structure; (IV) is properly controlled for the safety of the dog; and (V) allows the dog to extend to full stride, play, and engage in other types of mentally stimulating and social behaviors; or (ii) if the dealer obtains a certification from the attending veterinarian stating that a dog should not have unrestricted access to an outdoor exercise area for a specific medical reason, an alternative exercise plan prescribed by the veterinarian for the dog that meets the applicable requirements under section 3.8 of title 9, Code of Federal Regulations (or successor regulations); (E) that each dog has meaningful socialization with humans and compatible dogs for at least 30 minutes each day that\u2014 (i) includes positive interaction with a human such as petting, stroking, grooming, feeding, playing with, exercising, or other touching of the dog that is beneficial to the well-being of the dog; and (ii) does not include time spent in veterinary care; (F) that each dog receives adequate veterinary care, including\u2014 (i) prompt treatment of any disease, illness, or injury by a licensed veterinarian; (ii) a thorough, hands-on examination by a licensed veterinarian at least once each year, which shall include a dental exam; (iii) core vaccinations recommended by the latest version of the American Animal Hospital Association Canine Vaccination Guidelines; and (iv) medications to prevent intestinal parasites, heartworm disease, fleas, and ticks that are approved by a licensed veterinarian for canine use; (G) with respect to safe breeding practices for dogs, including\u2014 (i) a screening program for known prevalent inheritable diseases that may be disabling or likely to significantly affect the lifespan or quality of life of the mother or the offspring; (ii) prohibiting breeding, unless each dog bred\u2014 (I) has been screened by a licensed veterinarian prior to each attempt to breed; and (II) is found in the screening under subclause (I) to be free from health conditions that may be disabling to, or likely to significantly affect the lifespan or quality of life of, the mother or the offspring; (iii) prohibiting the breeding of a female dog to produce\u2014 (I) more than 2 litters in any 18-month period; or (II) more than 6 litters during the lifetime of the dog; (iv) that a female dog of any small breed (having a maximum weight range at maturity that is less than 40 pounds) not be bred\u2014 (I) before reaching the age of 18 months; or (II) after reaching the age of 9 years; (v) that a female dog of any large breed (having an expected weight range at maturity that includes 40 or more pounds) not be bred\u2014 (I) before reaching the age of 2 years; or (II) after reaching the age of 7 years; and (vi) that any canine caesarian section be performed by a licensed veterinarian; (H) that dogs be housed with other dogs, unless health or behavioral issues make group housing unsafe; and (I) to make all reasonable efforts to find humane placement for retired breeding dogs\u2014 (i) such as with an adoptive family, rescue organization, or other appropriate owner for that dog; and (ii) not including selling at auction or otherwise placing a retired breeding dog with another breeder for breeding purposes. .\n##### (b) Conforming amendment\nSection 13(a)(2)(B) of the Animal Welfare Act ( 7 U.S.C. 2143(a)(2)(B) ) is amended by inserting subject to paragraph (9), before for exercise of dogs .\n##### (c) Regulations\nNot later than 18 months after the date of enactment of this Act, the Secretary shall issue final regulations establishing the standards for the care of dogs by dealers, as required by this section and the amendments made by this section.",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in Senate"
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
        "name": "Animals",
        "updateDate": "2026-05-19T21:20:31Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4437is.xml"
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
      "title": "Puppy Protection Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Puppy Protection Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Animal Welfare Act to establish additional requirements for dealers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:37Z"
    }
  ]
}
```
