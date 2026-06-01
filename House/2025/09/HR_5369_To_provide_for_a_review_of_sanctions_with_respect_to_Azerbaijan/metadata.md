# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5369
- Title: Azerbaijan Sanctions Review Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5369
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2026-05-01T08:09:12Z
- Update date including text: 2026-05-01T08:09:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5369",
    "number": "5369",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Azerbaijan Sanctions Review Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-01T08:09:12Z",
    "updateDateIncludingText": "2026-05-01T08:09:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-15T16:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "RI"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
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
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MA"
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
      "sponsorshipDate": "2025-10-06",
      "state": "DC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "RI"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "OH"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5369ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5369\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Ms. Titus introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for a review of sanctions with respect to Azerbaijan.\n#### 1. Short title\nThis Act may be cited as the Azerbaijan Sanctions Review Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn September 19, 2023, Azerbaijan launched a military assault on Nagorno-Karabakh, resulting in the forced displacement of the region\u2019s entire Armenian population following a 10-month blockade of the Lachin Corridor, which deprived Armenian civilians access to food, fuel, medicine and other essential goods.\n**(2)**\nAzerbaijan\u2019s blockade and forced displacement of Nagorno-Karabakh\u2019s Armenians followed a major escalation of the conflict during the 2020 Nagorno-Karabakh War, during which Azerbaijani military and government officials named in section 3(b) have committed war crimes and serious human rights violations, including the extrajudicial killing of Armenian civilians and prisoners of war; the arbitrary detention, forced disappearances, and torture of Armenian civilians and prisoners of war and other captives, and the deliberate targeting of civilian populations.\n**(3)**\nAzerbaijan\u2019s continued detainment, torture, extrajudicial execution, and other serious human rights violations against prisoners of war and captured civilians calls into serious question their commitment to human rights and ability to negotiate an equitable, lasting peace settlement.\n**(4)**\nReporting conducted in September 2022 by the United Nations Committee on the Elimination of Racial Discrimination expressed deep concern over [a]llegations of severe and grave human rights violations committed during the 2020 hostilities and beyond by Azerbaijani military forces against prisoners of war and other protected persons of Armenian ethnic or national origin\u2014including extrajudicial killings, torture and other ill-treatment and arbitrary detention .\n**(5)**\nThe Department of State\u2019s Country Reports on Human Rights Practices released in August 2025 documented credible reports of: arbitrary or unlawful killings; torture or cruel, inhuman, or degrading treatment or punishment; arbitrary arrest and detention; transnational repression against individuals in another country, and notes that the government [of Azerbaijan] did not take credible steps or action to identify and punish officials who committed human rights abuses. .\n**(6)**\nHuman rights organizations have consistently reported on Azerbaijan\u2019s abuse of prisoners of war and other human rights violations, including a report by Human Rights Watch in March 2021 that found Azerbaijani forces had abused ethnic Armenian prisoners of war and subjected them to cruel and degrading treatment and torture either when they were captured, during their transfer, or while in custody at various detention facilities .\n**(7)**\nReporting conducted in 2024 by Freedom House found that the Government of Azerbaijan acted upon a comprehensive, methodically implemented strategy to empty Nagorno-Karabakh of its ethnic Armenian population between 2020 and 2023 and engaged in a pattern of arbitrary detention, torture, and ill-treatment of Armenians who fell into Azerbaijani custody. .\n**(8)**\nIn December 2021, an International Court of Justice ruling ordered Azerbaijan to protect from violence and bodily harm Armenians detained during and since the 2020 Nagorno-Karabakh War.\n**(9)**\nAt least 23 prisoners of war and hostages are still detained illegally by Azerbaijan as of August 2025 according to the Armenian Government, with independent observers noting that the true number of detainees is likely much higher given the many individuals still missing, and the limited information available due to Azerbaijan\u2019s misrepresentation of their status in an attempt to justify their continued captivity.\n**(10)**\nFollowing Azerbaijan\u2019s offensive in 2023, numerous high-ranking Armenian officials in Nagorno-Karabakh were arrested and detained by Azerbaijan, including Ruben Vardanyan, Davit Manukyan, Davit Babayan, Levon Mnatsakanyan, Arkadi Ghukasyan, Bako Sahakyan, Arayik Harutyunyan, and Davit Ishkhanyan.\n**(11)**\nIn January 2025, Azerbaijan commenced sham trials of the aforementioned former officials of Nagorno-Karabakh in Baku\u2019s military court, where detainees have been denied due process, the right to a fair trial, the right to legal counsel of their own choosing, and have been charged on political grounds without evidence and in the absence of independent observers.\n**(12)**\nIn March 2025, Azerbaijan ordered the International Committee of the Red Cross (ICRC), the only entity in Azerbaijan with the authorization to visit Armenian prisoners of war and civilian captives, to leave the country.\n**(13)**\nInternational humanitarian law requires parties to an international armed conflict to treat prisoners of war humanely in all circumstances.\n**(14)**\nIt is a war crime to willfully kill, mistreat, or torture prisoners of war, or to willfully cause great suffering or serious injury to body or health.\n**(15)**\nIn addition to being bound by customary international law, Azerbaijan is a party to the Geneva Conventions, the International Covenant on Civil and Political Rights (ICCPR), and the European Convention on Human Rights (ECHR) which strictly forbid extrajudicial killings.\n**(16)**\nDespite its international legal obligations under the Geneva Conventions and repeated calls by the United States Government, Azerbaijan has not released all relevant persons and instead continues to detain new prisoners of war, hostages, and captured civilians, nor have those responsible for serious human rights violations and war crimes faced legal consequences.\n**(17)**\nFollowing the publication of the terms of the initialed peace agreement between Armenia and Azerbaijan in August 2025, it was confirmed the document omits provisions to ensure the release of Armenian prisoners of war or civilian captives, raising concerns as to Azerbaijan\u2019s commitment to ensuring a just, durable, and dignified peace in the region.\n**(18)**\nAmid fraught peace talks between Armenia and Azerbaijan, the immediate and unconditional release of Armenian prisoners of war, civilians, and political detainees would represent an important confidence building measure.\n**(19)**\nIn addition to its arbitrary detention of Armenian prisoners, Azerbaijan also has also unlawfully detained over 300 Azerbaijani journalists, human rights defenders, civic activists and opposition figures, with Azerbaijani authorities escalating civil society crackdowns in the months leading up to the COP29 Climate Summit in November 2024.\n**(20)**\nAzerbaijan\u2019s brutal repression of domestic political opposition is of grave concern for the human rights of Azerbaijanis.\n**(21)**\nThe detention and subsequent torture and ill-treatment of journalists like Radio Free Europe/Radio Liberty reporter Farid Mehralizada, critics of the Aliyev government like Dr. Gubad Ibadoghlu, and human rights advocates like Rufat Safarov, raises fundamental concerns about due process and the integrity of the legal proceedings against those who express political dissent in Azerbaijan.\n**(22)**\nAzerbaijan is designated as Not Free by Freedom House due to the absence of political rights, civil liberties, and rule of law.\n#### 3. Review of sanctions with respect to Azerbaijan\n##### (a) Determination\nNot later than 180 days after the date of the enactment of this Act, the President shall submit to the appropriate congressional committees a determination, including a detailed justification, of whether any person listed in subsection (b) meets the criteria for the imposition of sanctions pursuant to\u2014\n**(1)**\nsection 1263(b) of the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 2656 note); or\n**(2)**\nsection 7031(c) of the National Security, Department of State, and Related Programs Appropriations Act.\n##### (b) Persons listed\nThe persons listed in this subsection, which includes officials of Republic of Azerbaijan, are the following:\n**(1)**\nLieutenant General Hikmat Izzat oglu Mirzayev, Commander of the Special Forces.\n**(2)**\nLieutenant Colonel Elgun Aliyev, Chief of the Military Police.\n**(3)**\nColonel Elshan Sanaev, Commander of Azerbaijani Military 218th Commando Brigade.\n**(4)**\nLieutenant General Anvar Afandiyev, Commander of Azerbaijani Ground Forces.\n**(5)**\nMajor General Jeyhun Hasanov, Penitentiary Service of the Ministry of Justice.\n**(6)**\nAli Naghiyev, Chief of the State Security Services.\n**(7)**\nSamir Nuriyev, Chief of Staff to President Aliyev.\n**(8)**\nFuad Alasgarov, Assistant to the President for Law Enforcement and Military Affairs.\n**(9)**\nOrhan Samadov, Office of the General Prosecutor.\n**(10)**\nVugar Guliyev, Office of the General Prosecutor.\n**(11)**\nZiya Masurov, Office of the General Prosecutor.\n**(12)**\nParviz Mirhashimov, Office of the General Prosecutor.\n**(13)**\nBabakhan Hasanaliyev, Office of the General Prosecutor.\n**(14)**\nHamza Eldar Akbar oglu, Office of the General Prosecutor.\n**(15)**\nAlakbarov Valeh Hasan oglu, Office of the General Prosecutor.\n**(16)**\nFaiq Qaniyev, Judge at Baku Court on Grave Crimes.\n**(17)**\nMirza Khankishiyev, Judge at Baku Court on Grave Crimes.\n**(18)**\nIlham Mahmudov, Judge at Baku Court on Grave Crimes.\n**(19)**\nEldar Ismayilov, Judge at Baku Court on Grave Crimes.\n**(20)**\nJavid Huseynov, Judge at Baku Court on Grave Crimes.\n**(21)**\nSamir Aliyev, Judge at Baku Court on Grave Crimes.\n**(22)**\nAzad Madjidov, Judge at Baku Court on Grave Crimes.\n**(23)**\nZeynal Agayev, Judge at Baku Court on Grave Crimes.\n**(24)**\nSabuhi Huseynov, Judge at Baku Court on Grave Crimes.\n**(25)**\nAfgan Hajiyev, Judge at Baku Court on Grave Crimes.\n**(26)**\nTelman Huseynov, Judge at Baku Court on Grave Crimes.\n**(27)**\nAli Mammadov, Judge at Baku Court on Grave Crimes.\n**(28)**\nVusal Gurbanov, Narimanov District Court Judge.\n**(29)**\nKamranov Hafiz, Narimanov District Court Judge.\n**(30)**\nYusif Yusifov, Chief Investigator of the Investigation Department for Combating Organized Crime, Ministry of Internal Affairs.\n**(31)**\nAbbasov Mirzali Abdulali oglu, Baku Court of Appeals.\n**(32)**\nMajor General Abulfat Rzayev, Main Organized Crime Department, Ministry of Internal Affairs.\n**(33)**\nMammadov Elchin, First Deputy Prosecutor General.\n**(34)**\nLieutenant Fuad Rafael oglu Nabiyev, Azerbaijan Ministry of Defense.\n**(35)**\nElchin Guliyev, State Border Service of Azerbaijan.\n**(36)**\nIlham Mehdiyev, State Border Service of Azerbaijan.\n**(37)**\nVusal Sultanov, State Border Service of Azerbaijan.\n**(38)**\nAzad Alakbarov, State Border Service of Azerbaijan.\n**(39)**\nIsmayil Akbarov, State Border Service of Azerbaijan.\n**(40)**\nRamin Bagirov, State Border Service of Azerbaijan.\n**(41)**\nLieutenant Colonel Elg\u00fcn Aliyev, Military Police Department of the Ministry of Defence.\n**(42)**\nKarim Valiyev, Chief of the General Staff of the Azerbaijani Armed Forces.\n**(43)**\nNemat Avazov, Director of the Investigation Department, Office of the Prosecutor General.\n**(44)**\nTagiyev Azer Heydar oglu, Nasimi District Court Judge.\n**(45)**\nAli Hasanov, Head of the Department for Public and Political Issues.\n**(46)**\nMehman Ahmadov, Director of State Security Service Investigative Isolator and Temporary Detention Facility in Baku.\n**(47)**\nMajor General Hikmat Hasanov, Commander of the 1st Army Corps of Azerbaijan.\n**(48)**\nKamran Aliyev, Prosecutor General.\n**(49)**\nUlviyya Shukuruvo, Baku City Sabail District Court Judge.\n**(50)**\nElnur Ismayilov, Deputy of Baku Investigative Detention Center.\n**(51)**\nMajor General Mais Barkhudarov, Commander of the 1st Army Corps of Azerbaijan.\n**(52)**\nMajor General Zaur Sabir Memmedov, Deputy Head of Azerbaijan\u2019s Special Forces.\n**(53)**\nColonel Tehran Mensimov, Commander of the Nakhichevan Army\u2019s Special Forces.\n##### (c) Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations, Committee on Appropriations, and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs, Committee on Appropriations, and the Committee on Financial Services of the House of Representatives.",
      "versionDate": "2025-09-15",
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
        "name": "International Affairs",
        "updateDate": "2025-09-25T15:29:56Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5369ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a review of sanctions with respect to Azerbaijan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-25T06:55:49Z"
    },
    {
      "title": "Azerbaijan Sanctions Review Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-25T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Azerbaijan Sanctions Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-25T06:53:15Z"
    }
  ]
}
```
